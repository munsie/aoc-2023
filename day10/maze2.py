#!/usr/bin/env python3

LEFT   = ( -1,  0 )
RIGHT  = (  1,  0 )
TOP    = (  0, -1 )
BOTTOM = (  0,  1 )

PIPE_NEIGHBORS = {
    '.': [ ],
    '-': [ LEFT,   RIGHT ],
    '|': [ TOP,    BOTTOM ],
    'L': [ TOP,    RIGHT ],
    'F': [ BOTTOM, RIGHT ],
    'J': [ TOP,    LEFT ],
    '7': [ BOTTOM, LEFT ]
}

def read_maze(filename: str) -> [ [ str ] ]:
    with open(filename) as f:
        maze = []
        for line in f:
            maze.append([*line.rstrip()])
        return maze

def find_start(maze: [ [ str ] ]) -> (int, int):
    for y in range(len(maze)):
        try:
            return ( maze[y].index('S'), y )
        except:
            pass
    return ( -1, -1 )

def translate_pos(x: ( int, int ), y: ( int, int )) -> (int, int):
    return ( x[0] + y[0], x[1] + y[1] )
   
def get_pipe_type(maze: [ [ str ] ], pos: (int, int)) -> str:
    return maze[pos[1]][pos[0]]

def set_pipe_type(maze: [ [ str ] ], pos: (int, int), t: str) -> None:
    maze[pos[1]][pos[0]] = t

def get_neighbor_positions(maze: [ [ str ] ], pos: (int, int)) -> [ (int, int) ]:
    '''
    Returns the two connected neighbors for the specified position.
    '''
    p = get_pipe_type(maze, pos)
    return [ translate_pos(pos, n) for n in PIPE_NEIGHBORS[p] ]

def get_opposite_end(maze: [ [ str ] ], pos: (int, int), enter: (int, int)) -> (int, int):
    # get the two neighbor positions
    neighbors = get_neighbor_positions(maze, pos)
    # remove the one we entered from
    neighbors.remove(enter)
    # and the one remaining is the opposite end
    return neighbors[0]

def find_connected_neighbors(maze: [ [ str ] ], pos: (int, int)) -> [ (int, int) ]:
    '''
    Returns the connected neighbors when the starting position is an unknown pipe type.
    '''

    neighbors = []
    for n in [ LEFT, RIGHT, TOP, BOTTOM ]:
        # find the neighbor in the maze
        n_pos = translate_pos(pos, n)
        neighbor = get_pipe_type(maze, n_pos)

        # look at each of it's possible neighbors and if our specified pos is in the list, add that neighbor to the list
        n_neighbors = get_neighbor_positions(maze, n_pos)
        if pos in n_neighbors:
            neighbors.append(n_pos)

    return neighbors

def wrap_pos(pos: (int, int), bounds: (int, int)) -> (int, int):
    x = pos[0]
    while x < 0:
        x += bounds[0]
    while x >= bounds[0]:
        x -= bounds[0]
    y = pos[1]
    while y < 0:
        y += bounds[1]
    while y >= bounds[1]:
        y -= bounds[1]
    return (x, y)

def print_maze(maze: [ [ str ] ]) -> None:
    for m in maze:
        print(''.join(m))

def flood_fill(maze: [ [ str ] ], pos: (int, int), fill: str):
    bounds = (len(maze[0]), len(maze))
    q = [ pos ]
    while len(q) > 0:
        pos = q.pop()
        t = get_pipe_type(maze, pos)
        if t == 'X' or t == fill:
            continue
        set_pipe_type(maze, pos, fill)
        q.append(wrap_pos(translate_pos(pos, LEFT), bounds))
        q.append(wrap_pos(translate_pos(pos, RIGHT), bounds))
        q.append(wrap_pos(translate_pos(pos, TOP), bounds))
        q.append(wrap_pos(translate_pos(pos, BOTTOM), bounds))

if __name__ == '__main__':
    # read in maze
    maze = read_maze('input.txt')
    
    # find starting point
    path = [ find_start(maze) ]
    
    # find the connected neighbors and use the first one as our next pos
    path.append(find_connected_neighbors(maze, path[-1])[0])

    # generate the loop
    while path[-1] != path[0]:
        # get the other end of the pipe
        path.append(get_opposite_end(maze, path[-1], path[-2]))

    # remove the extra start position
    path.pop()

    # convert path back to bitmap
    for pos in path:
        maze[pos[1]][pos[0]] = 'X'

    # flood fill the outside by starting at the upper left and filling in anything that
    # is not 'X'
    flood_fill(maze, (0, 0), ' ')

    print_maze(maze)
    
    # count up all of the points inside the path
    count = 0
    for m in maze:
        count += sum(1 for p in m if (p != 'X' and p != ' '))
    print(count)

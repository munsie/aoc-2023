#!/usr/bin/env python3

LEFT   = ( -1,  0 )
RIGHT  = (  1,  0 )
TOP    = (  0, -1 )
BOTTOM = (  0,  1 )

PIPE_NEIGHBORS = {
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

    # furthest point is half the length of the path
    print(int(len(path) / 2))

from queue import Queue

maze = [
    ["#", "#", "#", "#", "S", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", "#", "#", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "X", "#", "#", "#", "#", "#", "#", "#"]
]

def display_maze(maze):
    maze_row = ''

    for row in maze:
        for tile in row:
            maze_row += ' ' + tile
        print(maze_row)
        maze_row = ''

def find_node(maze, node):
    maze_size = len(maze)
    row_size = len(maze[0])

    for row in range(maze_size):
        for col in range(row_size):
            if maze[row][col] == node:
                return (row, col)
            
def transform_to_graph(maze):
    graph = {}
    maze_size = len(maze)
    row_size = len(maze[0])

    for row in range(maze_size):
        for col in range(row_size):
            if maze[row][col] != '#':
                adj_nodes = []

                if row+1 < maze_size and maze[row+1][col] != '#': # DOWN
                    adj_nodes.append((row+1, col))
                if row-1 >= 0 and maze[row-1][col] != '#': # UP
                    adj_nodes.append((row-1, col))
                if col+1 < row_size and maze[row][col+1] != '#': # RIGHT
                    adj_nodes.append((row, col+1))
                if col-1 >= 0 and maze[row][col-1] != '#': # LEFT
                    adj_nodes.append((row, col-1))

                graph[(row, col)] = adj_nodes

    return graph

def solve_maze(maze, maze_graph, start_node, end_node):
    visited = []
    start_path = [start_node]
    q = Queue()
    q.put(start_path)

    while not q.empty():
        path = q.get()
        neighbours = maze_graph[path[-1]]

        for node in neighbours:
            if node == end_node:
                for coordinate in path:
                    row, col = coordinate
                    maze[row][col] = 'X'
                return maze
            
            if node not in visited:
                visited.append(node)
                new_path = path + [node]
                q.put(new_path)

start_node = find_node(maze, 'S')
end_node = find_node(maze, 'X')
maze_graph = transform_to_graph(maze)

solved_maze = solve_maze(maze, maze_graph, start_node, end_node)
display_maze(maze)
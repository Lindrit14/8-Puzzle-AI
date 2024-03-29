#implement the a_star algorithm with heuristic for 8 Puzzle task
from gameLogic import display_puzzle
from puzzleFunctions import generate_puzzle
from gameLogic import display_puzzle



import heapq
class PuzzleState:
    def __init__(self, state, parent=None, action=None, cost=0 ):
        """
        Initialize a new puzzle state.

        Parameters:
        - state: The current state of the puzzle, typically represented as a list of lists.
        - parent (optional): The preceding puzzle state from which this state was derived.
        - action (optional): The move or action taken to reach the current state from the parent.
        - cost (optional): The cumulative cost to reach this state from the initial state.

        Each puzzle state represents a snapshot in the progression of solving the puzzle.
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost 
        
    def __lt__(self, other):
        """
        Define the less-than operation for PuzzleState objects for ordering purposes.

        Parameters:
        - other: Another instance of PuzzleState to compare against.

        Returns:
        - boolean: Result of comparison between this state and the other state.

        """
       
        return self.state < other.state


def calculate_manhattan(state, goal_state):
    """
    Calculate the Manhattan distance between the current state and the goal state.

    Parameters:
    - state: The current state of the puzzle, typically a 3x3 matrix.
    - goal_state: The desired goal state of the puzzle, also a 3x3 matrix.

    Returns:
    - distance: The total Manhattan distance of all tiles from their goal positions.

    """
    distance = 0
    for i in range(3):  
        for j in range(3):
            if state[i][j] == 0:
                continue
            
            goal_tile_position = next((gi, gj) for gi, row in enumerate(goal_state) for gj, val in enumerate(row) if val == state[i][j])
            
            distance += abs(goal_tile_position[0] - i) + abs(goal_tile_position[1] - j)
    return distance


def calculate_hamming(state, goal_state):
    """
    Calculate the Hamming distance heuristic for A* algorithm.

    Parameters:
    state (list of list of int): The current state of the puzzle, as a 2D list.
    goal_state (list of list of int): The goal state of the puzzle, as a 2D list.

    Returns:
    int: The Hamming distance between the current state and the goal state.
    """
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                distance += 1
    return distance

def generate_moves(node):
    """
    Generate all possible moves and their resulting states from the given node.

    Parameters:
    - node: The current node or state of the puzzle from which to generate moves.

    Returns:
    - moves: A list of PuzzleState instances representing the states after each possible move.

    """
    moves = []
    zero_position = next((ix, iy) for ix, row in enumerate(node.state) for iy, i in enumerate(row) if i == 0)
    x, y = zero_position

    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3: 
            new_state = [list(row) for row in node.state] 
            
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
           
            new_node = PuzzleState(new_state, node, (dx, dy), node.cost + 1)
            moves.append(new_node)
    return moves

def reconstruct_path(end_node):
    """
    Reconstruct the path from the end node to the start node by following parent links.

    Parameters:
    - end_node: The final node or state of the puzzle after reaching the goal.

    Returns:
    - path: A list of states representing the sequence of moves from the start to the goal.

    """
    path = []
    current_node = end_node
    while current_node is not None:
        path.insert(0, current_node.state)  
        current_node = current_node.parent
    return path


def a_star(start, goal, heuristic):
    """
    Implement the A* search algorithm to find the shortest path from start to goal.

    Parameters:
    - start: The initial state of the puzzle.
    - goal: The goal state of the puzzle.
    - heuristic: A function that estimates the cost from the current state to the goal.

    Returns:
    - The sequence of states from the start to the goal, representing the solution path.

    """
   
    total_nodes_generated = 0

  
    start_node = PuzzleState(start, None, None, 0)
    start_node.heuristic = heuristic(start_node.state, goal)  
    goal_node = PuzzleState(goal, None, None, 0)

   
    open_list = []
    heapq.heappush(open_list, (start_node.heuristic, start_node))  
    closed_list = set()

    while open_list:
       
        _, current_node = heapq.heappop(open_list)
        
        
        if current_node.state == goal_node.state:
            return reconstruct_path(current_node), total_nodes_generated  

        
        children = generate_moves(current_node)

        
        total_nodes_generated += len(children)

        for child in children:
            if tuple(map(tuple, child.state)) in closed_list:
                continue

            child.cost = current_node.cost + 1  
            child.heuristic = heuristic(child.state, goal)  

            
            heapq.heappush(open_list, (child.cost + child.heuristic, child))

        
        closed_list.add(tuple(map(tuple, current_node.state)))

    return None, total_nodes_generated




# start = [
#     [1, 5, 2],
#     [3, 6, 7],
#     [8, 4, 0]
# ]
# goal = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]

# solution_path, nodes_expanded = a_star(start, goal, calculate_hamming)

# # Print the solution path in a readable format
# if solution_path:
#     for step in solution_path:
#         display_puzzle(step)
#         print()  
# else:
#     print("No solution found.")

# print(f"Total nodes expanded: {nodes_expanded}")


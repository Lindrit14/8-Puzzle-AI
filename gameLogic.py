import puzzleFunctions

def move(puzzle, direction):
    """
    Move the blank space (denoted as 0) in the given direction if possible.

    The function calculates the new position of the blank space after the move
    and swaps the blank with the target tile. It returns the new state of the
    puzzle after the move. If the move is not possible (e.g., trying to move
    the blank space out of the puzzle's bounds), it returns the original state.

    Parameters:
    puzzle (list of list of int): The current state of the puzzle represented as a 2D list.
    direction (str): The direction to move the blank space. One of 'up', 'down', 'left', or 'right'.

    Returns:
    list of list of int: The new state of the puzzle after the move.
    """
   
    x, y = next((i, j) for i, row in enumerate(puzzle) for j, val in enumerate(row) if val == 0)

    
    moves = {
        'up': (1, 0),
        'down': (-1, 0),
        'left': (0, 1),
        'right': (0, -1),
    }

    
    dx, dy = moves.get(direction, (0, 0))

   
    new_x, new_y = x + dx, y + dy

   
    if 0 <= new_x < len(puzzle) and 0 <= new_y < len(puzzle[0]):
        
        new_puzzle = [row[:] for row in puzzle]

        
        new_puzzle[x][y], new_puzzle[new_x][new_y] = new_puzzle[new_x][new_y], new_puzzle[x][y]

        return new_puzzle  

    return puzzle 


def display_puzzle(state):
    for row in state:
        print(' '.join(str(n) for n in row))



def get_user_move():
    """
    Display the puzzle state in a human-readable format.

    The function prints the puzzle to the console with each tile represented by its number.
    The blank space (0) is displayed as an empty space for better readability.

    Parameters:
    puzzle (list of list of int): The puzzle state to display.
    """
    move = input("Enter your move (up, down, left, right): ")
    while move not in ['up', 'down', 'left', 'right']:
        move = input("Invalid move. Enter your move (up, down, left, right): ")
    return move


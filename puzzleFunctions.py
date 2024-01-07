import random

def count_inversions(arr):
    """
    Count the number of inversions in an array.
    
    An inversion is a pair of elements in an array, where the larger element 
    is ahead of the smaller one. This function is used to help determine if an 
    8-puzzle is solvable by checking the number of inversions in the flattened puzzle.
    
    Parameters:
    arr (list): A list of integers representing the puzzle.

    Returns:
    int: The number of inversions in the array.
    """
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j] and arr[i] != 0 and arr[j] != 0:
                inversions += 1
    return inversions

def is_solvable(puzzle):
    """
    Determine if an 8-puzzle is solvable.
    
    For an 8-puzzle to be solvable, the number of inversions must be even. This function 
    calculates the total number of inversions in the puzzle and returns True if the number 
    is even, indicating that the puzzle is solvable.
    
    Parameters:
    puzzle (list of list of int): The 8-puzzle represented as a 2D list.

    Returns:
    bool: True if the puzzle is solvable, False otherwise.
    """
    inversions = count_inversions([j for sub in puzzle for j in sub])
    return inversions % 2 == 0

def generate_puzzle():
    """
    Generate a random 8-puzzle.
    
    This function creates a solvable 8-puzzle by randomly shuffling the numbers 0-8 
    and arranging them in a 3x3 matrix. The function ensures that the generated puzzle 
    is solvable before returning it.

    Returns:
    list of list of int: A 2D list representing a solvable 8-puzzle.
    """
    while True:
        puzzle = [i for i in range(9)]  
        random.shuffle(puzzle)  
        puzzle = [puzzle[i:i+3] for i in range(0, 9, 3)]  

        if(is_solvable(puzzle)):
            return puzzle

def goal_state(current_state_of_puzzle):
    """
    Check if the current state of the puzzle matches the goal state.
    
    The goal state of an 8-puzzle is traditionally the numbers 1-8 in order 
    with the empty space (0) at the end. This function compares the current 
    state of the puzzle to this goal state.

    Parameters:
    current_state_of_puzzle (list of list of int): The current state of the 8-puzzle.

    Returns:
    bool: True if the current state is the goal state, False otherwise.
    """
    goal_state_puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
     
    for i in range(3):
        for j in range(3):
            if current_state_of_puzzle[i][j] != goal_state_puzzle[i][j]:
                return False
    return True

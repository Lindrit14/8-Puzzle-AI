import random

def generate_puzzle():
    while True:
        puzzle = [i for i in range(9)]  
        random.shuffle(puzzle)  
        puzzle = [puzzle[i:i+3] for i in range(0, 9, 3)]  

        return puzzle

def count_inversions(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j] and arr[i] != 0 and arr[j] != 0:
                inversions += 1
    return inversions

def is_solvable(puzzle):
    inversions = count_inversions([j for sub in puzzle for j in sub])
    return inversions % 2 == 0

def goal_state(current_state_of_puzzle):
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

# testing
randomPuzzle = generate_puzzle()

goal_state_puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

for row in randomPuzzle:
    print(row)
    
if(is_solvable(randomPuzzle)):
    print("This Puzzle is solvable")
else:
    print("This puzzle is not solvable")
    
# print(randomPuzzle)
# print(goal_state_puzzle)
# print(goal_state(randomPuzzle))
# print(goal_state(goal_state_puzzle))


# if(type(randomPuzzle) == type(goal_state_puzzle)):
#     print("They have the same type!")
# else:
#     print("They don't have the same type!")
import puzzleFunctions
import gameLogic

def play():
    puzzle = puzzleFunctions.generate_puzzle()
    print("Welcome to the 8-puzzle game! Arrange the numbers in order by making moves.")
    print("The empty space is represented by 0. You need to get it to the following configuration:")
    print("1 2 3\n4 5 6\n7 8 0\n")
    print("Here's your puzzle:")
    
    while not puzzleFunctions.goal_state(puzzle):
        gameLogic.display_puzzle(puzzle)
        move_direction = gameLogic.get_user_move()
        puzzle = gameLogic.move(puzzle, move_direction)
    
    gameLogic.display_puzzle(puzzle)
    print("Congratulations! You've solved the puzzle.")

play()
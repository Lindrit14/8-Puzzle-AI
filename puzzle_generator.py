# puzzle_generator.py
import json
from puzzleFunctions import generate_puzzle

def save_puzzles(file_name, puzzles):
    with open(file_name, 'w') as file:
        json.dump(puzzles, file)

def main():
    puzzles = []
    while len(puzzles) < 100:
        puzzle = generate_puzzle()
        puzzles.append(puzzle)

    save_puzzles('puzzles.txt', puzzles)

if __name__ == '__main__':
    main()

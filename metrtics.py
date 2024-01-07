import time
import statistics
import json
from puzzleFunctions import generate_puzzle
import a_star
from datetime import datetime  


goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

def read_puzzles(file_name):
    with open(file_name, 'r') as file:
        puzzles = json.load(file)
    return puzzles

def time_algorithm(algorithm, puzzles, heuristic):
    """
    Time the algorithm over multiple puzzles and return various metrics.

    Parameters:
    algorithm (function): The function to solve the puzzles, e.g., a_star.
    puzzles (list): List of puzzles to solve.
    heuristic (str): The heuristic to use ('manhattan' or 'hamming').

    Returns:
    dict: Dictionary of metrics including total time, mean execution time, standard deviation of time,
          total nodes generated, mean memory usage, and standard deviation of memory usage.
    """
    times = []
    moves_counts = []
    total_nodes = 0
    memory_usages = []

    for puzzle in puzzles:
        start_time = time.time()
        path, nodes_generated = algorithm(puzzle, goal_state,heuristic)  
        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        moves_counts.append(len(path) if path else 0)
        total_nodes += nodes_generated
        memory_usages.append(len(path) if path else 0) 

    total_time = sum(times)
    mean_time = statistics.mean(times)
    std_dev_time = statistics.stdev(times)
    mean_memory_usage = statistics.mean(memory_usages)
    std_dev_memory_usage = statistics.stdev(memory_usages)

    return {
        'total_time': total_time,
        'mean_time': mean_time,
        'std_dev_time': std_dev_time,
        'total_nodes': total_nodes,
        'mean_memory_usage': mean_memory_usage,
        'std_dev_memory_usage': std_dev_memory_usage
    }
    


puzzles = read_puzzles('puzzles.txt')


manhattan_metrics = time_algorithm(a_star.a_star, puzzles, a_star.calculate_manhattan )

hamming_metrics = time_algorithm(a_star.a_star, puzzles, a_star.calculate_hamming)


with open("results_log.txt", "a") as file:
    file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    file.write("---MANHATTAN---\n")
    file.write(f"Total Time: {manhattan_metrics['total_time']} seconds\n")
    file.write(f"Total Nodes: {manhattan_metrics['total_nodes']}\n")
    file.write(f"Mean Time: {manhattan_metrics['mean_time']} seconds\n")
    file.write(f"Standard Deviation Time: {manhattan_metrics['std_dev_time']}\n")
    file.write(f"Mean Memory Usage: {manhattan_metrics['mean_memory_usage']} Nodes\n")
    file.write(f"Standard Deviation Memory Usage: {manhattan_metrics['std_dev_memory_usage']}\n")
    
    file.write("---HAMMING---\n")
    file.write(f"Total Time: {hamming_metrics['total_time']} seconds\n")
    file.write(f"Total Nodes: {hamming_metrics['total_nodes']}\n")
    file.write(f"Mean Time: {hamming_metrics['mean_time']} seconds\n")
    file.write(f"Standard Deviation Time: {hamming_metrics['std_dev_time']}\n")
    file.write(f"Mean Memory Usage: {hamming_metrics['mean_memory_usage']} Nodes\n")
    file.write(f"Standard Deviation Memory Usage: {hamming_metrics['std_dev_memory_usage']}\n")
    file.write("\n")  

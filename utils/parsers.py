"""
Common parsing utilities for Advent of Code challenges.
Reusable functions to parse different input formats.
"""
from io import TextIOWrapper
from typing import List, Tuple, Dict, Any, Callable, TypeVar
import re
from .clock import clock
from .input import get_input_file_from_script_file

T = TypeVar('T')

def load_input(script_file: str, parser: Callable[[TextIOWrapper], T]) -> T:
    """
    Load and parse input file with automatic timing.
    
    Args:
        script_file: Pass __file__ from your main.py
        parser: Parsing function (e.g., parse_lines, parse_ints, etc.)
    
    Returns:
        Parsed data
    
    Example:
        data = load_input(__file__, parse_lines)
        data = load_input(__file__, parse_digit_grid)
    """
    clock.start('file_loading')
    file = get_input_file_from_script_file(script_file)
    clock.stop('file_loading', 'File loading time')
    
    clock.start('data_parsing')
    data = parser(file)
    clock.stop('data_parsing', 'Data parsing time')
    return data


def parse_lines(file: TextIOWrapper) -> List[str]:
    """
    Parse input as list of strings (one per line).
    
    Returns: ["str1", "str2", "str3", ...]
    
    Example input:
        hello
        world
    Returns: ["hello", "world"]
    """
    return [line.strip() for line in file.readlines()]


def parse_ints(file: TextIOWrapper) -> List[int]:
    """
    Parse input as list of integers (one per line).
    
    Returns: [1, 2, 3, ...]
    
    Example input:
        42
        100
        -5
    Returns: [42, 100, -5]
    """
    return [int(line.strip()) for line in file.readlines()]


def parse_int_lists(file: TextIOWrapper, delimiter: str = None) -> List[List[int]]:
    """
    Parse input as lists of integers (space or custom delimiter separated).
    
    Args:
        delimiter: Separator between numbers (default: whitespace)
    
    Returns: [[1, 2], [3, 4], ...]
    
    Example input:
        1 2 3
        4 5 6
    Returns: [[1, 2, 3], [4, 5, 6]]
    """
    return [list(map(int, line.strip().split(delimiter))) for line in file.readlines()]


def parse_grid(file: TextIOWrapper) -> List[List[str]]:
    """
    Parse input as 2D grid of characters.
    
    Returns: [['a','b'], ['c','d'], ...]
    
    Example input:
        abc
        def
    Returns: [['a','b','c'], ['d','e','f']]
    """
    return [[char for char in line.strip()] for line in file.readlines()]


def parse_digit_grid(file: TextIOWrapper) -> List[List[int]]:
    """
    Parse input as 2D grid of single digits.
    
    Returns: [[1,2], [3,4], ...]
    
    Example input:
        123
        456
    Returns: [[1,2,3], [4,5,6]]
    """
    return [[int(char) for char in line.strip()] for line in file.readlines()]


def parse_csv(file: TextIOWrapper, delimiter: str = ',') -> List[str]:
    """
    Parse single line CSV input.
    
    Args:
        delimiter: Separator character (default: comma)
    
    Returns: ['val1', 'val2', ...]
    
    Example input:
        apple,banana,cherry
    Returns: ['apple', 'banana', 'cherry']
    """
    return file.read().strip().split(delimiter)


def parse_csv_ints(file: TextIOWrapper, delimiter: str = ',') -> List[int]:
    """
    Parse single line CSV of integers.
    
    Args:
        delimiter: Separator character (default: comma)
    
    Returns: [1, 2, 3, ...]
    
    Example input:
        10,20,30
    Returns: [10, 20, 30]
    """
    return list(map(int, file.read().strip().split(delimiter)))


def parse_blocks(file: TextIOWrapper, delimiter: str = '\n\n') -> List[str]:
    """
    Parse input separated by blank lines (or custom delimiter).
    
    Args:
        delimiter: Block separator (default: double newline)
    
    Returns: ['block1', 'block2', ...]
    
    Example input:
        line1
        line2

        line3
        line4
    Returns: ['line1\nline2', 'line3\nline4']
    """
    return file.read().strip().split(delimiter)


def parse_grid_with_positions(file: TextIOWrapper, 
                              target_chars: str = None) -> Tuple[List[List[str]], Dict[str, List[Tuple[int, int]]]]:
    """
    Parse grid and return both the grid and positions of specific characters.
    
    Args:
        target_chars: Characters to track positions for (default: all non-space chars)
    
    Returns: (grid, positions_dict)
        grid: 2D array of characters
        positions_dict: {char: [(row, col), ...]}
    
    Example input:
        .#.
        #.#
    Returns: ([['.',#','.'], ['#','.',#']], {'#': [(0,1), (1,0), (1,2)], '.': [(0,0), (0,2), (1,1)]})
    """
    grid = [[char for char in line.strip()] for line in file.readlines()]
    positions = {}
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col]
            if target_chars is None or char in target_chars:
                if char not in positions:
                    positions[char] = []
                positions[char].append((row, col))
    
    return grid, positions


def parse_custom(file: TextIOWrapper, 
                line_parser: Callable[[str], T]) -> List[T]:
    """
    Parse input with a custom parser function for each line.
    
    Args:
        line_parser: Function that takes a line string and returns parsed data
    
    Returns: List of parsed results
    
    Example:
        def my_parser(line):
            parts = line.split()
            return (parts[0], int(parts[1]))
        
        data = parse_custom(file, my_parser)
    """
    return [line_parser(line.strip()) for line in file.readlines()]

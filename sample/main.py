from typing import List
from utils import (
    load_input,
    deep_copy_arg, 
    solution_print,
    parse_lines,
)

# TODO: Define the appropriate data type based on the chosen parser
DataType = List[str]


@deep_copy_arg()
def part_one_solution(data: DataType) -> int:
    result = 0

    # TODO: Implement solution
    
    return result


def part_two_solution(data: DataType) -> int:
    result = 0
    
    # TODO: Implement solution
    
    return result

def run():
    # load_input automatically handles file opening and timing
    # Quick reference:
    # data = load_input(__file__, parse_lines)              → ["str1", "str2", ...]
    # data = load_input(__file__, parse_ints)               → [1, 2, 3, ...]
    # data = load_input(__file__, parse_int_lists)          → [[1,2], [3,4], ...]
    # data = load_input(__file__, parse_grid)               → [['a','b'], ['c','d'], ...]
    # data = load_input(__file__, parse_digit_grid)         → [[1,2], [3,4], ...]
    # data = load_input(__file__, parse_csv)                → ['val1', 'val2', ...]
    # data = load_input(__file__, parse_csv_ints)           → [1, 2, 3, ...]
    # data = load_input(__file__, parse_blocks)             → ['block1', 'block2', ...]
    # data = load_input(__file__, parse_grid_with_positions)→ (grid, {'#': [(0,1), (1,2)], ...})
    
    data = load_input(__file__, parse_lines)

    solution_print(1, lambda: part_one_solution(data))
    solution_print(2, lambda: part_two_solution(data))


if __name__ == "__main__":
    run()

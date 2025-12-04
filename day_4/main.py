from typing import Dict, List, Tuple
from utils import (
    load_input,
    deep_copy_arg, 
    solution_print,
    parse_lines,
    MapUtils
)
from utils.parsers import parse_grid_to_positions, parse_grid_with_positions

DataType = Tuple[Tuple[int, int], List[List[str]], Dict[Tuple[int, int], str]]

def compute(data) -> Tuple[int, List[Tuple[int, int]]]:
    result = 0
    max_rolls_around = 4
    list_rolls_removed = []
    sizegrid, grid, positions = data 
    map_str = '\n'.join(''.join(row) for row in grid)
    map_utils = MapUtils(map_str)
    
    for i in range(sizegrid[0]):
        for j in range(sizegrid[1]):
            if positions[(i,j)] == "@":
                rolls_around = 0
                around = map_utils.get_positions_around((j, i))

                for pos in around.values():
                    if(map_utils.get_cell_value_from_position(pos) == "@"):
                        rolls_around += 1
                if rolls_around < max_rolls_around:
                    result += 1
                    list_rolls_removed.append((i, j))
            
    return result, list_rolls_removed

@deep_copy_arg()
def part_one_solution(data: DataType) -> int:
    result = 0
    max_rolls_around = 4
    sizegrid, grid, positions = data 
    map_str = '\n'.join(''.join(row) for row in grid)
    map_utils = MapUtils(map_str)
    for i in range(sizegrid[0]):
        for j in range(sizegrid[1]):
            if positions[(i,j)] == "@":
                rolls_around = 0
                around = map_utils.get_positions_around((j, i))

                for pos in around.values():
                    if(map_utils.get_cell_value_from_position(pos) == "@"):
                        rolls_around += 1
                if rolls_around < max_rolls_around:
                    result += 1
            
    return result


def part_two_solution(data: DataType) -> int:
    result = 0
    rounds = 0
    # we need to use compute again and again until no more rolls can be removed
    while True:
        rolls_removed, rolls_positions = compute(data)
        rounds += 1
        if rolls_removed == 0:
            break
        result += rolls_removed

        # remove the rolls from data
        sizegrid, grid, positions = data

        # transfome any roll position into 'x'
        for pos in rolls_positions:
            i, j = pos
            grid[i][j] = 'x'
            positions[(i, j)] = 'x'
        

        data = (sizegrid, grid, positions)
    #print(f"Total rounds: {rounds}")
    #print("\n".join(''.join(row) for row in grid))
    return result

def run():
    data = load_input(__file__, parse_grid_to_positions)
    solution_print(1, lambda: part_one_solution(data))
    solution_print(2, lambda: part_two_solution(data))


if __name__ == "__main__":
    run()

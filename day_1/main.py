from typing import List
import math
from utils import get_input_file_from_script_file, deep_copy_arg, solution_print, clock


@deep_copy_arg()
def part_one_solution(lines: List[str]) -> int:
    hit_0 = 0
    start_point = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        match direction:
            case 'L':
                start_point = (start_point - distance) % 100
            case 'R':
                start_point = (start_point + distance) % 100
        
        if start_point == 0:
            hit_0 += 1

    return hit_0

def part_two_solution(lines: List[str]) -> int:
    hit_0 = 0
    position = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            end_pos = position - distance
            hit_0 += math.floor((position - 1) / 100) - math.floor((end_pos - 1) / 100)
            position = end_pos % 100
        else: 
            end_pos = position + distance
            hit_0 += math.floor(end_pos / 100) - math.floor(position / 100)
            position = end_pos % 100

    return hit_0
def run():
    clock.start('data_loading')
    file = get_input_file_from_script_file(__file__)
    lines = [line.strip() for line in file.readlines()]
    clock.stop('data_loading', 'Data loading time')

    solution_print(1, lambda: part_one_solution(lines))
    solution_print(2, lambda: part_two_solution(lines))

if __name__ == "__main__":
    run()
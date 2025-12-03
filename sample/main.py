from io import TextIOWrapper
from typing import List
from utils import get_input_file_from_script_file, deep_copy_arg, solution_print, clock

lines_type = list[tuple[int, int]]


def prepare_data(file: TextIOWrapper) -> lines_type:
    return []


@deep_copy_arg()
def part_one_solution(lines:  lines_type) -> int:

    return 0


def part_two_solution(lines: lines_type) -> int:

    return 0


def run():
    clock.start('data_loading')
    file = get_input_file_from_script_file(__file__)
    data = prepare_data(file)
    clock.stop('data_loading', 'Data loading time')

    solution_print(1, lambda: part_one_solution(data))
    solution_print(2, lambda: part_two_solution(data))


if __name__ == "__main__":
    run()

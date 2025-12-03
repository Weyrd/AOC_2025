from io import TextIOWrapper
from typing import List
from utils import get_input_file_from_script_file, deep_copy_arg, solution_print, clock
import heapq

lines_type = list[list[int]]


def prepare_data(file: TextIOWrapper) -> lines_type:
    lines = file.readlines()
    lines = [[int(num) for num in line.strip()] for line in lines]
    return lines


@deep_copy_arg()
def part_one_solution(lines:  lines_type) -> int:
    total = 0
    for line in lines:
        # line = [5,8,9,2,1] we need to find biggest number we can make (92 here)
        biggest_number_of_line = heapq.nlargest(1, line)
        index_max = line.index(biggest_number_of_line[0])
        first_digit = biggest_number_of_line[0]

        # if index_max is last index, take the second biggest number
        if index_max == len(line) - 1:
            biggest_number_of_line = heapq.nlargest(2, line)
            index_max = line.index(biggest_number_of_line[-1])
            first_digit = biggest_number_of_line[-1]

        # split the line and take the last part
        last_part = line[index_max + 1:]
        second_digit = heapq.nlargest(1, last_part)[0]

        total += int(str(first_digit) + str(second_digit))

    return total


def part_two_solution(lines: lines_type, battery_num: int) -> int:
    total = 0
    for line in lines:
        result = 0
        index_cut = 0
        
        for i in range(battery_num):
            end_idx = len(line) - battery_num + i + 1
            split_line = line[index_cut:end_idx]
            
            biggest_number = max(split_line)
            index = split_line.index(biggest_number)
            
            result = result * 10 + biggest_number # shift left and add digit
            index_cut += index + 1
        
        total += result
    return total


def run():
    clock.start('data_loading')
    file = get_input_file_from_script_file(__file__)
    data = prepare_data(file)
    clock.stop('data_loading', 'Data loading time')

    solution_print(1, lambda: part_two_solution(data, 2)) # part 2 is more opti, i keep part 1 for reference
    solution_print(2, lambda: part_two_solution(data, 12))


if __name__ == "__main__":
    run()

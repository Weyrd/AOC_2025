from typing import List
from utils import get_input_file_from_script_file, deep_copy_arg, solution_print, clock

def check_is_valid_number_part1(number: int) -> tuple[bool, int]:
    str_number = str(number)
    if len(str_number) % 2 != 0:
        return True, 0
    
    half_len = len(str_number) // 2
    first_half = str_number[:half_len]
    second_half = str_number[half_len:]

    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            return True, 0
    return False, number

def check_is_valid_number_part2(number: int) -> tuple[bool, int]:
    str_number = str(number)

    # check if all digits are the same and more than 1 digit (1111, 222)
    if(len(set(str_number)) == 1 and len(str_number) > 1):
        return False, number
    
    # check for repeated patterns (1212, 123123)
    # we check for all possible group sizes from 1 to half the length of the number
    # skip group sizes that don't divide evenly into the total length
    # then we repeat the group X times to match the length of the number
    # then we check if the repeated group matches the original number
    for i in range(1, len(str_number) // 2 + 1):
        if len(str_number) % i != 0:
            continue
        group = str_number[:i]
        repeated_group = group * (len(str_number) // i)
        if repeated_group == str_number:
            return False, number
        
    return True, 0


@deep_copy_arg()
def part_one_solution(list_ids:  List[(int, int)]) -> int:
    invalid_numbers = []
    for start, end in list_ids:
        for number in range(start, end + 1):
            if not check_is_valid_number_part1(number)[0]:
                invalid_numbers.append(number)
    return sum(invalid_numbers)


def part_two_solution(list_ids: List[(int, int)]) -> int:
    invalid_numbers = []
    for start, end in list_ids:
        for number in range(start, end + 1):
            if not check_is_valid_number_part2(number)[0]:
                invalid_numbers.append(number)
    return sum(invalid_numbers)

def run():
    clock.start('data_loading')
    file = get_input_file_from_script_file(__file__)
    list_ids = [tuple(map(int, line.split("-"))) for line in [line.strip() for line in file.readlines()][0].split(",")]
    clock.stop('data_loading', 'Data loading time')
    
    solution_print(1, lambda: part_one_solution(list_ids))
    solution_print(2, lambda: part_two_solution(list_ids))

if __name__ == "__main__":
    run()
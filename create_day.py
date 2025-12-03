#!/usr/bin/env python3
"""
Utility script to create new Advent of Code day folders.
Usage: python create_day.py <day_number>
"""
import sys
import shutil
from pathlib import Path


def create_day(day_number: str) -> None:
    """
    Create a new day folder based on the sample template.
    
    Args:
        day_number: The day number to create (e.g., "3" for day_3)
    """
    try:
        day_int = int(day_number)
        if day_int < 1 or day_int > 25:
            print('\033[91mDay number must be between 1 and 25.\033[0m')
            sys.exit(1)
    except ValueError:
        print('\033[91mInvalid day number. Please provide a number between 1 and 25.\033[0m')
        sys.exit(1)
    
    # Setup paths
    project_root = Path(__file__).parent
    sample_dir = project_root / 'sample'
    day_dir = project_root / f'day_{day_number}'
    
    # Check if day already exists
    if day_dir.exists():
        print(f'\033[93mDay {day_number} was already created.\033[0m')
        return
    
    if not sample_dir.exists():
        print('\033[91mSample directory not found!\033[0m')
        sys.exit(1)
    
    day_dir.mkdir(exist_ok=True)
    
    # Copy main.py from sample
    sample_main = sample_dir / 'main.py'
    if sample_main.exists():
        shutil.copy2(sample_main, day_dir / 'main.py')
        print(f'\033[92m✓\033[0m Copied main.py from sample')
    else:
        print('\033[91mWarning: sample/main.py not found!\033[0m')
    
    # Create empty input.txt
    (day_dir / 'input.txt').touch()
    print(f'\033[92m✓\033[0m Created empty input.txt')
    
    print(f'\033[92m\nSuccessfully created day_{day_number}!\033[0m')
    print(f'\nYou can now:')
    print(f'  1. Add your puzzle input to \033[93mday_{day_number}/input.txt\033[0m')
    print(f'  2. Implement your solution in \033[93mday_{day_number}/main.py\033[0m')
    print(f'  3. Run with: \033[96mpython runner.py {day_number}\033[0m')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python create_day.py <day_number>')
        print('Example: python create_day.py 4')
        sys.exit(1)
    
    create_day(sys.argv[1])

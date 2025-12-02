import sys
from day_1.main import run as day_1
from day_2.main import run as day_2

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python runner.py <day_number>')
        sys.exit(1)

    day = sys.argv[1]

    match day:
        case '1':
            day_1()
        
        case '2':
            day_2()
        
        case _:
            print('No solution for this day.')
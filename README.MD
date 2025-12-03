# AOC_2025

## Installation / Dependencies

### Python

**Disclaimers:**

- It is recommended to execute the project in a [virtual environment](https://docs.python.org/3/library/venv.html).

```bash
pip install -r requirements.txt
```


## Creating a new day

To quickly scaffold a new day folder based on the sample template:

```bash
python create_day.py <day_number>
```

This will:
- Create a `day_<number>` folder
- Copy the template from `sample/main.py`
- Create an empty `input.txt` file
- Warn you if the day already exists

Example:
```bash
python create_day.py 4
```

## Parser Utilities

The project includes reusable parsing utilities to handle common AOC input formats. See [PARSER_REFERENCE.md](PARSER_REFERENCE.md) for detailed documentation.

Quick examples:
```python
from utils import parse_lines, parse_ints, parse_grid, parse_int_lists

# Parse lines as strings
data = parse_lines(file)  # ["str1", "str2", ...]

# Parse lines as integers
data = parse_ints(file)  # [1, 2, 3, ...]

# Parse 2D grid
data = parse_grid(file)  # [['a','b'], ['c','d'], ...]

# Parse space-separated integers
data = parse_int_lists(file)  # [[1,2,3], [4,5,6], ...]
```

Available parsers: `parse_lines`, `parse_ints`, `parse_int_lists`, `parse_grid`, `parse_digit_grid`, `parse_csv`, `parse_csv_ints`, `parse_blocks`, `parse_grid_with_positions`, `parse_custom`...

## Launching scripts

_Pre-requisite: Add your puzzle input to `day_<number>/input.txt`._

### Python

```bash
python runner.py <day_number>
```
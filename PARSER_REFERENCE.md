# Parser Utilities Reference

Quick guide for using the parsing utilities in your AOC solutions.

## Basic Parsers

### `parse_lines(file)` → `List[str]`
Parse each line as a string.
```python
# Input:
hello
world

# Output: ["hello", "world"]
```

### `parse_ints(file)` → `List[int]`
Parse each line as an integer.
```python
# Input:
42
100
-5

# Output: [42, 100, -5]
```

### `parse_int_lists(file)` → `List[List[int]]`
Parse space-separated integers on each line.
```python
# Input:
1 2 3
4 5 6

# Output: [[1, 2, 3], [4, 5, 6]]
```

## Grid Parsers

### `parse_grid(file)` → `List[List[str]]`
Parse as 2D grid of characters.
```python
# Input:
abc
def

# Output: [['a','b','c'], ['d','e','f']]
```

### `parse_digit_grid(file)` → `List[List[int]]`
Parse as 2D grid of single digits.
```python
# Input:
123
456

# Output: [[1,2,3], [4,5,6]]
```

### `parse_grid_with_positions(file, target_chars=None)` → `Tuple[grid, positions]`
Parse grid and track character positions.
```python
# Input:
.#.
#.#

# Output:
# grid: [['.','#','.'], ['#','.',#']]
# positions: {'#': [(0,1), (1,0), (1,2)], '.': [(0,0), (0,2), (1,1)]}
```

## CSV Parsers

### `parse_csv(file, delimiter=',')` → `List[str]`
Parse single line CSV.
```python
# Input:
apple,banana,cherry

# Output: ['apple', 'banana', 'cherry']
```

### `parse_csv_ints(file, delimiter=',')` → `List[int]`
Parse single line CSV of integers.
```python
# Input:
10,20,30

# Output: [10, 20, 30]
```

## Block Parsers

### `parse_blocks(file, delimiter='\n\n')` → `List[str]`
Parse blocks separated by blank lines.
```python
# Input:
line1
line2

line3
line4

# Output: ['line1\nline2', 'line3\nline4']
```


## Advanced Parsers

### `parse_custom(file, line_parser)` → `List[Any]`
Use a custom parser function for each line.
```python
def my_parser(line):
    parts = line.split()
    return (parts[0], int(parts[1]))

data = parse_custom(file, my_parser)
# Input: "apple 5" → Output: [('apple', 5), ...]
```
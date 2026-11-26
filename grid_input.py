
from validation import validate_grid, validate_dictionary


def parse_grid_input(raw_grid):
    """
    Convert text input into a 2D letter grid.

    Example:
    o a a n
    e t a e
    i h k r
    i f l v
    """

    if not isinstance(raw_grid, str) or not raw_grid.strip():
        raise ValueError("Grid input cannot be empty.")

    rows = []

    for line in raw_grid.strip().splitlines():

        line = line.strip()

        if not line:
            continue

        if any(char.isspace() for char in line):
            row = line.split()
        else:
            row = list(line)

        rows.append(row)

    return validate_grid(rows)


def parse_dictionary_input(raw_dictionary):
    """
    Convert comma-separated or newline-separated text
    into a validated dictionary list.
    """

    if not isinstance(raw_dictionary, str) or not raw_dictionary.strip():
        raise ValueError("Dictionary input cannot be empty.")

    words = raw_dictionary.replace(",", "\n").splitlines()

    return validate_dictionary(words)

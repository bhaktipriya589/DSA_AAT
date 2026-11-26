
def validate_grid(grid):
    """
    Validate and normalize a rectangular lowercase-letter grid.
    Returns the normalized grid.
    """

    if not isinstance(grid, list) or not grid:
        raise ValueError("Grid cannot be empty.")

    if len(grid) > 10:
        raise ValueError("Grid cannot have more than 10 rows.")

    normalized_grid = []
    expected_columns = None

    for row in grid:

        if not isinstance(row, list) or not row:
            raise ValueError("Grid rows cannot be empty.")

        if expected_columns is None:
            expected_columns = len(row)

        if len(row) != expected_columns:
            raise ValueError("Grid must be rectangular.")

        if len(row) > 10:
            raise ValueError("Grid cannot have more than 10 columns.")

        normalized_row = []

        for cell in row:

            if not isinstance(cell, str):
                raise ValueError("Grid cells must contain letters.")

            cell = cell.strip().lower()

            if len(cell) != 1 or not cell.isalpha() or not cell.isascii():
                raise ValueError("Each grid cell must contain one English letter.")

            normalized_row.append(cell)

        normalized_grid.append(normalized_row)

    return normalized_grid


def validate_dictionary(words):
    """
    Validate, normalize and remove duplicate dictionary words.
    Returns a list of unique lowercase words.
    """

    if not isinstance(words, list) or not words:
        raise ValueError("Dictionary cannot be empty.")

    if len(words) > 10000:
        raise ValueError("Dictionary cannot contain more than 10,000 words.")

    valid_words = []
    seen = set()

    for word in words:

        if not isinstance(word, str):
            raise ValueError("Dictionary entries must be strings.")

        word = word.strip().lower()

        if not word:
            continue

        if len(word) > 10:
            raise ValueError("Each dictionary word must have at most 10 characters.")

        if not word.isalpha() or not word.isascii():
            raise ValueError(
                f"Invalid dictionary word: {word}"
            )

        if word not in seen:
            seen.add(word)
            valid_words.append(word)

    if not valid_words:
        raise ValueError("Dictionary must contain at least one valid word.")

    return valid_words

def display_welcome():
    """Display the application welcome message."""

    print("\n========================================")
    print("          WORD SEARCH SOLVER")
    print("========================================")
    print("Find dictionary words hidden in a letter grid!")
    print("\nInstructions:")
    print("- Enter letters separated by spaces or without spaces.")
    print("- Enter one row per line.")
    print("- Separate dictionary words using commas.")
    print("- Grid dimensions must not exceed 10 x 10.")
    print("- Dictionary words can contain up to 10 letters.")
    print("========================================\n")


def get_user_input():
    """
    Collect grid and dictionary input from the user.

    Returns:
        raw_grid: Grid entered as multiline text.
        raw_dictionary: Dictionary entered as text.
    """

    print("Enter your letter grid.")
    print("Press Enter on an empty line when finished.\n")

    grid_rows = []

    while True:
        row = input()

        if not row.strip():
            break

        grid_rows.append(row)

    raw_grid = "\n".join(grid_rows)

    print("\nEnter dictionary words separated by commas:")
    raw_dictionary = input()

    return raw_grid, raw_dictionary
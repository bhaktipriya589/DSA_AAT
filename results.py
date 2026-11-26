def display_results(results):
    """
    Display all dictionary words found in the grid
    along with their grid positions.
    """

    print("\n========== WORD SEARCH RESULTS ==========")

    if not results:
        print("No dictionary words were found in the grid.")
        return

    print(f"\nTotal words found: {len(results)}")

    for word, path in sorted(results.items()):

        print(f"\nWord: {word.upper()}")

        print("Coordinates (row, column):")

        formatted_path = " -> ".join(
            f"({row}, {col})" for row, col in path
        )

        print(formatted_path)

    print("\n=========================================")
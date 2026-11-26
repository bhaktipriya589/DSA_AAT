from trie import Trie


# Allowed movements: up, down, left, right
DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def find_words(grid, dictionary):
    """
    Find all dictionary words present in the grid.

    Returns:
        Dictionary containing:
        word: list of (row, column) coordinates
    """

    if not grid or not dictionary:
        return {}

    rows = len(grid)
    cols = len(grid[0])

    # Build Trie using dictionary words
    trie = Trie()

    for word in dictionary:
        trie.insert(word)

    found_words = {}

    # DFS with backtracking
    def dfs(row, col, node, visited, path):

        # Current grid letter
        letter = grid[row][col].lower()

        # Stop if the letter is not a valid Trie prefix
        if letter not in node.children:
            return

        next_node = node.children[letter]

        # Mark current cell as visited
        visited.add((row, col))
        path.append((row, col))

        # Check whether a complete word is found
        if next_node.is_end_of_word:

            word = "".join(grid[r][c].lower() for r, c in path)

            if word not in found_words:
                found_words[word] = path.copy()

        # Explore neighbouring cells
        for dr, dc in DIRECTIONS:

            new_row = row + dr
            new_col = col + dc

            # Check grid boundaries
            if not (0 <= new_row < rows):
                continue

            if not (0 <= new_col < cols):
                continue

            # Do not reuse an already visited cell
            if (new_row, new_col) in visited:
                continue

            dfs(
                new_row,
                new_col,
                next_node,
                visited,
                path
            )

        # Backtracking: remove current cell
        path.pop()
        visited.remove((row, col))

    # Start DFS from every grid cell
    for row in range(rows):
        for col in range(cols):

            dfs(
                row,
                col,
                trie.root,
                set(),
                []
            )

    return found_words
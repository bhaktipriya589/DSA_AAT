# The Expedition's Lost Words – Word Search Solver

## Project Overview

The Expedition's Lost Words is a Python-based word search application that finds dictionary words hidden inside a two-dimensional letter grid.

The application uses a **Trie data structure** combined with **Depth-First Search (DFS)** and **backtracking** to efficiently search for words while avoiding unnecessary exploration.

A Streamlit interface allows users to enter a letter grid and dictionary words and view the results visually.

## Features

- Interactive letter grid with selectable rows and columns.
- Supports grids up to 10 × 10.
- Dictionary input using commas or new lines.
- Input validation for grid and dictionary entries.
- Trie-based prefix searching.
- DFS with backtracking.
- Horizontal and vertical word searching.
- Prevents reusing a cell within the same word.
- Finds multiple dictionary words.
- Highlights every found word using different colours.
- Displays coordinate paths using 1-based indexing.
- Handles cases where no dictionary words are found.

## Technologies Used

- Python
- Streamlit
- Trie
- Depth-First Search (DFS)
- Backtracking

## Project Structure

```text
DSA_AAT/
│
├── main.py          # Main application entry point
├── interface.py     # Streamlit user interface
├── results.py       # Displays search results and highlights
├── trie.py          # Trie implementation
├── word_search.py   # DFS and backtracking algorithm
├── validation.py    # Input validation
├── grid_input.py    # Grid and dictionary parsing
└── README.md        # Project documentation
```

## Algorithm Explanation

### 1. Trie

The Trie stores dictionary words character by character.

It supports efficient prefix checking, allowing the search algorithm to stop exploring a path when the current sequence is not a valid prefix of any dictionary word.

### 2. Depth-First Search

DFS explores neighbouring cells in four directions:

- Up
- Down
- Left
- Right

Each cell is checked against the current Trie node.

### 3. Backtracking

A visited set prevents a cell from being reused within the same word search.

After exploring a path, the algorithm removes the current cell from the visited set so that other paths can use it.

### 4. Prefix Pruning

If a character does not exist in the current Trie node's children, the search stops immediately along that path.

This avoids exploring paths that cannot produce dictionary words.

## Complexity Analysis

Let:

- D = Total number of characters across all dictionary words.
- R = Number of grid rows.
- C = Number of grid columns.
- L = Maximum dictionary word length.

**Trie Construction:** O(D)

**DFS Search:** In the worst case, the search explores paths of length up to L from each grid cell. With four initial directions and no cell reuse, a loose upper bound is O(R × C × 4 × 3^(L-1)).

Trie prefix pruning reduces unnecessary exploration in practice.

**Space Complexity:** O(D + R × C + L), excluding the storage of the returned word paths.

## How to Run the Project

### Prerequisites

- Python installed.
- pip package manager.

### Installation

Install Streamlit:

```bash
pip install streamlit
```

### Run the Application

Open a terminal in the project directory and execute:

```bash
python -m streamlit run main.py
```

The application will open in your web browser.

## How to Use

1. Select the number of rows and columns.
2. Enter one letter in each grid cell.
3. Enter dictionary words separated by commas or new lines.
4. Click **Find Words**.
5. View the matching words, highlighted grid, colour legend, and coordinate paths.

## Team Contributions

| Member | Contribution |
|---|---|
| Member 1 | Input validation and grid/dictionary parsing |
| Member 2 | Trie implementation and word-search algorithm |
| Member 3 | Streamlit interface and result visualization |

## Repository

GitHub: https://github.com/bhaktipriya589/DSA_AAT
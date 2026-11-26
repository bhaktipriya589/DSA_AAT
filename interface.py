import streamlit as st


def display_welcome():
    """Display the application heading and instructions."""

    st.title("🔎 Word Search Solver")

    st.write(
        "Recover hidden words from a letter grid using "
        "Trie, prefix search and DFS with backtracking."
    )

    st.divider()


def get_user_input():
    """Collect grid letters using individual input boxes."""

    st.subheader("1. Create Your Letter Grid")

    st.caption(
        "Choose the grid dimensions, then enter one English letter "
        "in each box. Maximum size: 10 × 10."
    )

    dimension_col1, dimension_col2 = st.columns(2)

    with dimension_col1:
        rows = st.number_input(
            "Number of rows",
            min_value=1,
            max_value=10,
            value=4,
            step=1
        )

    with dimension_col2:
        cols = st.number_input(
            "Number of columns",
            min_value=1,
            max_value=10,
            value=4,
            step=1
        )

    st.markdown("**Enter your letters**")

    grid = []

    for row_index in range(int(rows)):

        st.caption(f"Row {row_index + 1}")

        row_values = []
        input_columns = st.columns(int(cols))

        for col_index in range(int(cols)):

            with input_columns[col_index]:

                letter = st.text_input(
                    f"R{row_index + 1} C{col_index + 1}",
                    max_chars=1,
                    key=f"grid_cell_{row_index}_{col_index}",
                    label_visibility="collapsed"
                )

                row_values.append(letter.strip())

        grid.append(row_values)

    st.divider()

    st.subheader("2. Enter Dictionary Words")

    st.caption(
        "Enter the candidate words separated by commas or new lines."
    )

    raw_dictionary = st.text_area(
        "Dictionary",
        height=120,
        placeholder="",
        label_visibility="collapsed"
    )

    st.divider()

    submitted = st.button(
        "🔍 Find Words",
        type="primary",
        use_container_width=True
    )

    # Check that every grid cell contains a letter
    raw_grid = "\n".join(
        " ".join(row) for row in grid
    )

    if submitted:

        if any(not letter for row in grid for letter in row):
            st.error("Please fill in every letter box before searching.")
            submitted = False

    return raw_grid, raw_dictionary, submitted
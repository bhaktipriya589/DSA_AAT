import streamlit as st


WORD_COLORS = [
    "#22C55E",
    "#38BDF8",
    "#F59E0B",
    "#C084FC",
    "#F472B6",
    "#F87171",
    "#2DD4BF",
    "#A3E635",
    "#818CF8",
    "#FB923C"
]


def display_results(grid, results):
    """
    Display all found words with different colours
    and highlight their paths on the letter grid.
    """

    # Handle the case when no words are found
    if not results:
        st.markdown(
            """
            <div style="
                background-color: #FFF4CC;
                color: #6B5500;
                padding: 14px 16px;
                border-radius: 10px;
                border: 1px solid #F0D98A;
                font-weight: 600;
                margin: 10px 0;
            ">
                No dictionary words were found in the grid.
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    st.markdown("### 🏆 Search Results")
    st.success(f"Successfully found {len(results)} word(s)!")

    words = sorted(results.keys())

    # Assign a unique colour to each found word
    word_colors = {
        word: WORD_COLORS[index % len(WORD_COLORS)]
        for index, word in enumerate(words)
    }

    # Store the colours belonging to each grid cell
    cell_colors = {}

    for word, path in results.items():

        for coordinate in path:

            if coordinate not in cell_colors:
                cell_colors[coordinate] = []

            cell_colors[coordinate].append(word_colors[word])

    st.markdown("### 🔎 Highlighted Letter Grid")

    grid_html = f"""
    <style>
    .letter-grid {{
        display: grid;
        grid-template-columns: repeat({len(grid[0])}, minmax(0, 1fr));
        gap: 9px;
        max-width: 500px;
        margin: 20px auto;
    }}

    .letter-cell {{
        aspect-ratio: 1 / 1;
        background: #FFFFFF;
        border: 2px solid #D9D5E8;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #29263D;
        font-size: 25px;
        font-weight: bold;
        box-shadow: 0 2px 5px rgba(80, 65, 130, 0.08);
    }}
    </style>

    <div class="letter-grid">
    """

    # Generate each grid cell
    for row_index, row in enumerate(grid):

        for col_index, letter in enumerate(row):

            coordinate = (row_index, col_index)
            colors = cell_colors.get(coordinate, [])

            if colors:

                # Give shared cells a split-colour background
                segment_size = 100 / len(colors)

                gradient_parts = []

                for index, color in enumerate(colors):

                    start = index * segment_size
                    end = (index + 1) * segment_size

                    gradient_parts.append(
                        f"{color} {start:.2f}% {end:.2f}%"
                    )

                background = (
                    "linear-gradient(135deg, "
                    + ", ".join(gradient_parts)
                    + ")"
                )

                border_color = colors[0]

            else:
                background = "#FFFFFF"
                border_color = "#D9D5E8"

            grid_html += f"""
            <div class="letter-cell"
                 style="background: {background};
                        border-color: {border_color};">
                {letter.upper()}
            </div>
            """

    grid_html += "</div>"

    st.html(grid_html)

    # Display the colour legend
    st.markdown("### 🎨 Word Colour Legend")

    legend_columns = st.columns(2)

    for index, word in enumerate(words):

        with legend_columns[index % 2]:

            color = word_colors[word]

            st.markdown(
                f"""
                <div style="
                    display:flex;
                    align-items:center;
                    gap:10px;
                    margin:8px 0;
                    padding:10px;
                    border-radius:8px;
                    background:#FFFFFF;
                    border:1px solid #E3E0EF;
                ">
                    <div style="
                        width:16px;
                        height:16px;
                        border-radius:4px;
                        background:{color};
                        flex-shrink:0;
                    "></div>
                    <span style="
                        color:#29263D;
                        font-weight:bold;
                    ">
                        {word.upper()}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Display each word and its individual path
    st.markdown("### 📍 Found Words and Their Paths")

    for word in words:

        path = results[word]

        formatted_path = " → ".join(
            f"({row + 1}, {col + 1})"
            for row, col in path
        )

        color = word_colors[word]

        with st.container(border=True):

            st.markdown(
                f"<span style='color:{color};font-weight:bold;'>"
                f"● {word.upper()}</span>",
                unsafe_allow_html=True
            )

            st.code(formatted_path, language=None)
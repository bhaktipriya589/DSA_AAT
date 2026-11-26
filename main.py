import streamlit as st

from grid_input import parse_grid_input, parse_dictionary_input
from word_search import find_words
from interface import display_welcome, get_user_input
from results import display_results


def main():

     
    st.set_page_config(
    page_title="Word Search Solver",
    page_icon="🔎",
    layout="centered"
    )

    st.markdown("""
    <style>
    .stApp {
        background-color: #F8F7FC;
        color: #29263D;
    }

    h1, h2, h3 {
        color: #5145A5 !important;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: white !important;
        color: #29263D !important;
        border: 1px solid #D9D5E8;
        border-radius: 8px;
    }

    .stButton > button {
        background-color: #6255B5;
        color: white;
        border-radius: 9px;
        border: none;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #5145A5;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    display_welcome()

    raw_grid, raw_dictionary, submitted = get_user_input()

    if submitted:

        try:
            if not raw_grid.strip():
                st.error("Please enter a letter grid.")

            elif not raw_dictionary.strip():
                st.error("Please enter dictionary words.")

            else:
                # Validate and parse input
                grid = parse_grid_input(raw_grid)
                dictionary = parse_dictionary_input(raw_dictionary)

                # Find words using Trie and DFS
                results = find_words(grid, dictionary)
                # Display results
                st.subheader("Search Results")

                display_results(grid, results)
                 
        except ValueError as error:
            st.error(f"Input Error: {error}")

        except Exception as error:
            st.error(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
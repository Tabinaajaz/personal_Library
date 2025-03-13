import streamlit as st
import pandas as pd

# Load or create book database
BOOKS_FILE = "books.csv"

try:
    books_df = pd.read_csv(BOOKS_FILE)
except FileNotFoundError:
    books_df = pd.DataFrame(columns=["Title", "Author", "Genre", "Year", "Status"])

st.title("📚 Personal Library Manager")

# Add a new book
st.sidebar.header("📖 Add a New Book")
title = st.sidebar.text_input("Book Title")
author = st.sidebar.text_input("Author")
genre = st.sidebar.text_input("Genre")
year = st.sidebar.number_input("Year", min_value=1000, max_value=2100, step=1)
status = st.sidebar.selectbox("Status", ["Unread", "Reading", "Read"])

if st.sidebar.button("Add Book"):
    new_book = pd.DataFrame([[title, author, genre, year, status]], columns=books_df.columns)
    books_df = pd.concat([books_df, new_book], ignore_index=True)
    books_df.to_csv(BOOKS_FILE, index=False)
    st.sidebar.success(f"✅ '{title}' added successfully!")

# Display the library
st.subheader("📚 My Book Collection")
if not books_df.empty:
    st.dataframe(books_df)

    # Search books
    search_term = st.text_input("🔍 Search by Title or Author")
    if search_term:
        filtered_books = books_df[
            books_df["Title"].str.contains(search_term, case=False, na=False) |
            books_df["Author"].str.contains(search_term, case=False, na=False)
        ]
        st.dataframe(filtered_books)

    # Remove book
    remove_title = st.selectbox("❌ Remove a Book", books_df["Title"])
    if st.button("Remove Book"):
        books_df = books_df[books_df["Title"] != remove_title]
        books_df.to_csv(BOOKS_FILE, index=False)
        st.success(f"🚮 '{remove_title}' removed successfully!")

else:
    st.warning("📭 No books in your collection yet. Add one!")


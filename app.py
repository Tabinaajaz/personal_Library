import json
import os

# File to store library data
LIBRARY_FILE = "library.json"

# Load library from file if it exists
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    # Validate year input
    if not year.isdigit():
        print("Invalid year! Please enter a valid number.")
        return
    
    book = {
        "Title": title,
        "Author": author,
        "Year": int(year),
        "Genre": genre,
        "Read": read_status
    }
    library.append(book)
    save_library(library)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        key = "Title"
    elif choice == "2":
        key = "Author"
    else:
        print("Invalid choice!")
        return

    query = input(f"Enter the {key.lower()}: ").strip().lower()
    matches = [book for book in library if query in book[key].lower()]
    
    if matches:
        print("\nMatching Books:")
        for i, book in enumerate(matches, start=1):
            print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    
    print("\nYour Library:")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty.")
        return
    
    read_books = sum(1 for book in library if book["Read"])
    percentage_read = (read_books / total_books) * 100
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

# Main menu
def main():
    library = load_library()
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
# This script provides a simple command-line interface for managing a personal library.
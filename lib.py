library = []

# Add 3 books
for i in range(1):
    print(f"\nEnter details for Book ")
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    library.append([book_id, title, author, year])

# Display books
print("\n--- Library Books ---")
for b in library:
    print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Year: {b[3]}")

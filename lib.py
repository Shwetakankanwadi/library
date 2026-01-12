library = []

with open("books.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        library.append(data)

print("\n--- Library Books ---")
for b in library:
    print(f"ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Year: {b[3]}")

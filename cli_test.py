import requests

BASE_URL = "http://127.0.0.1:5000"

def view_all_books():
    res = requests.get(f"{BASE_URL}/books")
    for book in res.json():
        print(book)

def view_book():
    book_id = input("Enter book ID: ")
    res = requests.get(f"{BASE_URL}/books/{book_id}")
    if res.status_code == 200:
        print(res.json())
    else:
        print("Book not found.")

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    res = requests.post(f"{BASE_URL}/books", json={
        "title": title,
        "author": author,
        "year": int(year)
    })
    print("Added:", res.json())

def update_book():
    book_id = input("Enter book ID to update: ")
    title = input("New title (leave blank to skip): ")
    author = input("New author (leave blank to skip): ")
    year = input("New year (leave blank to skip): ")
    data = {}
    if title: data["title"] = title
    if author: data["author"] = author
    if year: data["year"] = int(year)

    res = requests.put(f"{BASE_URL}/books/{book_id}", json=data)
    if res.status_code == 200:
        print("Updated:", res.json())
    else:
        print("Book not found.")

def delete_book():
    book_id = input("Enter book ID to delete: ")
    res = requests.delete(f"{BASE_URL}/books/{book_id}")
    if res.status_code == 200:
        print("Deleted:", res.json())
    else:
        print("Book not found.")

def menu():
    while True:
        print("\n📚 Book API Menu:")
        print("1. View all books")
        print("2. View book by ID")
        print("3. Add a book")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            view_all_books()
        elif choice == "2":
            view_book()
        elif choice == "3":
            add_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()

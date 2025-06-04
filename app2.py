from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Book API!"})

@app.route("/books", methods=["GET"])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    books = cursor.execute("SELECT * FROM books").fetchall()
    conn.close()
    return jsonify([dict(book) for book in books])

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    conn.close()
    if book:
        return jsonify(dict(book))
    return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    year = data.get("year")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": new_id, "title": title, "author": author, "year": year}), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not book:
        conn.close()
        return jsonify({"error": "Book not found"}), 404

    title = data.get("title", book["title"])
    author = data.get("author", book["author"])
    year = data.get("year", book["year"])

    conn.execute("UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?", (title, author, year, book_id))
    conn.commit()
    conn.close()

    return jsonify({"id": book_id, "title": title, "author": author, "year": year})

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not book:
        conn.close()
        return jsonify({"error": "Book not found"}), 404

    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted", "book": dict(book)})

if __name__ == "__main__":
    app.run(debug=True)
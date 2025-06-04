# 📚 Book CRUD API

This project is a simple Book Management system with full **CRUD** functionality using:

- `app1.py`: A Flask-based REST API tested via Postman.
- `app2.py` + `cli_test.py`: A command-line interface for interacting with the same database.
- `books.db`: An SQLite database storing book records.

---

## 📁 Project Structure

```
book-crud-api/
├── app1.py        # First version: Flask API using Postman
├── app2.py        # Backend logic separated for CLI use
├── cli_test.py         # Command-line interface for managing books
├── books.db       # SQLite database
```

---

## 🚀 How to Use

### 🌐 1. Run the Flask API (`app1.py`)

Use this if you want to access your data through a web API and test with Postman.

```bash
python app1.py
```

#### 🔗 API Endpoints:

- `GET /books` — Get all books  
- `GET /books/<id>` — Get one book by ID  
- `POST /books` — Add a new book (send JSON)  
- `PUT /books/<id>` — Update a book  
- `DELETE /books/<id>` — Delete a book  

Use **Postman** or `curl` to test the API.

---

### 🖥️ 2. Use the CLI (`cli_test.py` + `app2.py`)

Use this to interact with the database via terminal commands.

```bash
python cli_test.py
```

You’ll get an interactive menu to:

- View all books
- View a book by ID
- Add a book
- Update a book
- Delete a book

---

## ⚙️ Setup

Install Flask (for API):

```bash
pip install flask
```

Ensure `books.db` is in the same directory.

---

## 🧪 GitHub Workflow

```bash
# Clone the repo
git clone https://github.com/Jacques961/book-crud-api.git

# Add your files
git add .

# Commit your changes
git commit -m "Initial commit: Add Flask API, CLI, and database"

# Push to GitHub
git push origin main
```

---

## 📝 Notes

- The CLI is simpler for internal/local usage.
- The API version is more flexible for external integration.
- Both versions share the same `books.db` SQLite file.

---

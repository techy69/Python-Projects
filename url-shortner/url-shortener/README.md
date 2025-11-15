<<<<<<< HEAD
# URL Shortener

Simple Flask-based URL shortener example.

Files:

- `app.py` - Flask application
- `models.py` - SQLAlchemy model
- `templates/` - HTML templates
- `static/style.css` - basic styles

Quick start:

1. Create a virtual environment (recommended):

   python -m venv .venv
   .venv\Scripts\Activate.ps1 # PowerShell on Windows

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app:

   python app.py

Open http://127.0.0.1:5000 in your browser.

Note: `db.sqlite3` will be created on first run; do not commit it to version control.
=======
# Python-Projects
A collection of Python projects showcasing various programming concepts, algorithms, and real-world applications developed during my B.C.A journey at UPES

## Projects

### 1. Unit Converter

A versatile unit converter that supports length, temperature, and currency conversions.

#### Usage Examples:

```bash
# Length
python unit_converter.py length 5 km m
# Output: 5 km = 5000.00 m

# Temperature
python unit_converter.py temperature 100 C F
# Output: 100 C = 212.00 F

# Currency
python unit_converter.py currency 100 USD INR
# Output: 100 USD = 8300.00 INR
```

### 2. TODO List Manager

A command-line TODO list application with beautiful formatting using the Rich library.

**Installation:**

```bash
pip install rich
```

#### Usage Examples:

```bash
# Add tasks
python todo.py add "Finish Python project"
python todo.py add "Push to GitHub"

# List tasks
python todo.py list

# Mark a task done
python todo.py done 1

# Delete a task
python todo.py delete 2
```

### 3. Personal Notes - Flask Web Application

A lightweight personal notes management system built with Flask and SQLite. Full CRUD (Create, Read, Update, Delete) functionality with a clean, responsive web interface.

**Features:**
- Create, view, edit, and delete notes
- SQLite database for local storage
- Flash messages for user feedback
- Responsive design with modern UI
- MVC architecture implementation

**Tech Stack:** Flask 2.3.2, Flask-SQLAlchemy 3.0.3, SQLite3, HTML/CSS, Jinja2

**Installation:**

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
# Access at http://127.0.0.1:5000
```

**Usage Examples:**

```bash
# Create a new note
- Click "+ New Note" button
- Enter title and body content
- Click "Save"

# View all notes
- Homepage displays all notes sorted by last updated

# Edit a note
- Click on note title to view
- Click "Edit" button
- Modify content and click "Update"

# Delete a note
- Open the note
- Click "Delete" button
- Confirm deletion
```

**Project Structure:**
```
personal-notes/
├── app.py              # Main Flask application
├── models.py           # Database models
├── static/style.css    # Stylesheet
└── templates/          # HTML templates
```
>>>>>>> 5f5498a4d3d637182f9d03095a82af6a0ef13781

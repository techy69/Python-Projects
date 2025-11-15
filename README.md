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

### 4. URL Shortener - Flask Web Application

A Flask-based URL shortener that allows users to create short, memorable links for long URLs. Features include custom alias support, click tracking, and a clean web interface.

**Features:**
- Shorten long URLs to compact links
- Custom alias support for personalized short URLs
- Click tracking and analytics
- SQLite database for URL storage
- Responsive web design
- URL validation and duplicate checking

**Tech Stack:** Flask 2.3.2, Flask-SQLAlchemy 3.0.3, SQLite3, HTML/CSS, Jinja2

**Installation:**

```bash
# Navigate to the url-shortner directory
cd url-shortner

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
# Access at http://127.0.0.1:5000
```

**Usage Examples:**

```bash
# Create a short URL
- Enter long URL in the input field
- Optionally provide a custom alias
- Click "Shorten" button
- Copy the generated short URL

# Access shortened URL
- Visit http://127.0.0.1:5000/[short_code]
- Automatically redirects to original URL
- Click count is tracked

# View all URLs
- Homepage displays all shortened URLs
- Shows original URL, short code, and click count
```

**Project Structure:**

```
url-shortner/
├── app.py              # Main Flask application
├── models.py           # Database models
├── static/             # CSS and static files
│   └── style.css       # Stylesheet
├── templates/          # HTML templates
│   ├── index.html      # Homepage
│   └── error.html      # Error page
├── requirements.txt    # Python dependencies
└── urls.db            # SQLite database (auto-created)
```

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


```markdown
# Flask Regex Matcher 🔍

A simple Flask web app that uses Python’s `re` module to find words containing both **"ra"** and **"pp"**.  
It provides a clean HTML/CSS interface for testing regex patterns.

---

## Features
- Input text through a web form
- Regex matching with Python’s `re` module
- Styled results with HTML & CSS
- Easy to run locally with Flask

---

## Project Structure
```
flask_regex_app/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/Muntazer72/flask-regex-matcher.git
cd flask-regex-matcher
```

### 2. Create a virtual environment
- **Windows (PowerShell/Command Prompt):**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **Linux/macOS (bash/zsh):**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

You’ll know it’s active when your terminal prompt starts with `(venv)`.

---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Run the app
```bash
python app.py
```

---

### 5. Open in browser
Visit:
```
http://127.0.0.1:5000/
```

---

## Example Input
```
grapple wrapper trapped rapid apple approach
```

## Example Output
```
grapple
wrapper
trapped
```

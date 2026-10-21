# 🔐 Password Strength Checker

## Project Overview

The Password Strength Checker is a Python-based web application developed to evaluate password strength and help users understand basic password security practices.

The application uses Streamlit to provide a simple, interactive, and attractive user interface.

## Objectives

- Evaluate password strength using predefined rules.
- Check password length and character variety.
- Identify selected common passwords and predictable patterns.
- Display a password strength score.
- Provide suggestions for improving password security.

## Features

- Password input with hidden characters.
- Strength score displayed out of 100.
- Four categories: Weak, Fair, Strong, and Very Strong.
- Visual progress bar.
- Password security checklist.
- Suggestions for creating stronger passwords.
- Dark-themed user interface.

## Technologies Used

- Python
- Streamlit
- Regular Expressions (`re`)
- HTML and CSS styling through Streamlit

## Project Structure

```text
PasswordStrengthChecker/
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Installation

1. Install Python on your computer.
2. Download or clone this project.
3. Open a terminal in the project directory.
4. Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run the following command in the terminal:

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## Testing

Use sample passwords to test the application, including common passwords and longer passwords containing different character types.

The displayed score is based on predefined rules and should be treated as an educational estimate.

## Limitations

- The scoring system is rule-based and is not a complete security assessment.
- The application checks only a limited set of common passwords and predictable patterns.
- It does not check passwords against a comprehensive data-breach database.
- A high score does not guarantee that a password is completely secure.

## Conclusion

This project demonstrates how Python and Streamlit can be used to build a password strength evaluation tool. It provides immediate feedback and encourages users to follow better password security practices.

## Author

**Name:** [Mansi parkellu]  
**Project:** Password Strength Checker  
**Program:** IBM Cybersecurity Bootcamp

# 🔐 Password Strength Analyzer

A clean, beginner-friendly Python command-line utility designed to analyze password complexity, evaluate overall strength, and suggest actionable security improvements.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Aesthetics](https://img.shields.io/badge/UI-ANSI%20Color-magenta.svg)

---

## ✨ Features

- **Interactive Console Interface:** Prompts users for passwords and analyzes them on-the-fly.
- **Robust Evaluation Criteria:** Evaluates password based on:
  - Minimum standard length (8+ characters)
  - Preferred strong length (12+ characters)
  - Lowercase characters (`a-z`)
  - Uppercase characters (`A-Z`)
  - Numeric digits (`0-9`)
  - Special characters (e.g., `!@#$%^&*()`)
- **Security-First Grading:** Passwords shorter than 8 characters are *always* rated as **Weak** since length is the single most critical factor against brute-force attacks.
- **Targeted Improvement Recommendations:** Offers custom instructions detailing exactly what makes the password insecure and how to correct it.
- **Cross-Platform Colorized Styling:** Leverages `colorama` for a vibrant console experience, falling back gracefully to plain text on terminals where it isn't installed.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
Ensure you have **Python 3.6 or higher** installed. Check your version with:
```bash
python --version
```

### 2. Clone/Copy the Codebase
Navigate to the directory containing the project:
```bash
cd password-strength-analyzer
```

### 3. Install Optional Dependencies (Highly Recommended)
To get the fully styled, colorized terminal UI, install `colorama` using `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Note: If you run the app without installing dependencies, it will work perfectly but display without ANSI color accents).*

---

## 🚀 Running the Analyzer

Run the main script using python:
```bash
python main.py
```

### Example Usage & Evaluation
When you run the app, you will see an interactive prompt. Here is how different inputs are evaluated:

- **Input:** `12345` -> **[ WEAK ]**
  - *Feedback:* Warning about character count (< 8) and missing upper, lower, numbers, and symbols.
- **Input:** `P@ssw0rdStrength!` -> **[ STRONG ]**
  - *Feedback:* High praise! All criteria ticked with custom color indicators `[✓]`.

To exit the analyzer loop, type `exit` or hit `Ctrl+C`.

---

## 📐 How Strength is Classified

We grade password security on a point system (from 0 to 5 points), corresponding to the criteria checklist met:

| Strength | Score Range | Description & Action |
| :--- | :--- | :--- |
| **🔴 Weak** | `0` to `2` points (or length `< 8`) | Critically vulnerable. Multiple criteria are unmet. Immediate updates are recommended. |
| **🟡 Medium** | `3` to `4` points (and length `≥ 8`) | Good foundation. Lacks a couple of dimensions (e.g., missing special characters or mixed case). |
| **🟢 Strong** | `5` points (and length `≥ 8`) | Excellent security. Met all complexity parameters. Extremely resistant to basic brute-forcing. |

---

## 💡 Password Security Tips

1. **Length is King:** A password's entropy (randomness) increases exponentially with its length. Aim for at least 12–16 characters!
2. **Use Passphrases:** Instead of a complex, unmemorable password like `P@$$w0rd!`, construct a passphrase out of 4-5 random words (e.g., `correct-horse-battery-staple`). They are easier to remember and much harder to crack.
3. **Never Reuse Passwords:** Utilize a secure Password Manager to generate and save unique credentials for each of your online accounts.

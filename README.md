# 📚 Awesome BscIT

> A curated, organized collection of practicals, lab exercises, and coursework from the **BScIT (Bachelor of Science in Information Technology)** program — covering Semester 1 and Semester 2 subjects.

[![PHP](https://img.shields.io/badge/PHP-8.x-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![HTML](https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Live%20Site-GitHub%20Pages-brightgreen?logo=github)](https://thvariableyt.github.io/Awesome-BscIT/)
[![Repo Size](https://img.shields.io/github/repo-size/ThVariableYT/Awesome-BscIT)](https://github.com/ThVariableYT/Awesome-BscIT)
[![Stars](https://img.shields.io/github/stars/ThVariableYT/Awesome-BscIT?style=social)](https://github.com/ThVariableYT/Awesome-BscIT/stargazers)

---

## 🌐 Live Website

This repository is deployed as a GitHub Pages site. You can browse all practicals interactively at:

🔗 **[https://thvariableyt.github.io/Awesome-BscIT/](https://thvariableyt.github.io/Awesome-BscIT/)**

The site is powered by `index.html` at the root and provides a clean browsing interface for navigating practicals by semester and subject.

---

## 📖 About This Repository

This is a personal academic repository maintained by **Jash Gandhi (ThVariableYT)** as part of the **FYIT (First Year Information Technology)** course under BScIT. It contains hands-on lab practicals organized by semester and subject, covering topics in web programming, Python, operating systems, and object-oriented programming.

The repository also serves as a **live reference website** (via GitHub Pages) — making it easy for fellow students to browse and learn from the practicals.

---

## 📂 Repository Structure

```
Awesome-BscIT/
│
├── Semester 1/
│   ├── IP/              # Introduction to Programming practicals
│   ├── OS/              # Operating Systems lab exercises
│   └── WP/              # Web Programming (HTML/CSS basics)
│
├── Semester 2/
│   ├── OOP/             # Object-Oriented Programming (Python)
│   ├── PADP/            # Problem Analysis & Design Principles
│   └── Web Programming/ # Advanced Web Programming (PHP, HTML)
│
├── .github/
│   └── workflows/       # GitHub Actions CI/CD (PHP & HTML validation)
│
├── index.html           # GitHub Pages landing site
├── .gitattributes       # Git line-ending normalization config
└── README.md            # This file
```

---

## 🗂️ Subjects Covered

### Semester 1

| Folder | Subject | Topics |
|--------|---------|--------|
| `IP/`  | Introduction to Programming | Basic programming concepts, control flow, functions |
| `OS/`  | Operating Systems | Shell commands, process management, file systems |
| `WP/`  | Web Programming | HTML structure, CSS styling, basic web pages |

### Semester 2

| Folder | Subject | Topics |
|--------|---------|--------|
| `OOP/` | Object-Oriented Programming | Classes, inheritance, polymorphism in Python |
| `PADP/` | Problem Analysis & Design Principles | Algorithms, flowcharts, pseudocode |
| `Web Programming/` | Web Programming | PHP scripting, forms, conditionals, loops, patterns |

---

## 🧩 Notable Practicals

Here are some examples of practicals included in this repository:

- **`Odd-Even.php`** — Determines if a given number is odd or even
- **`Greater Than.php`** — Compares two values and prints the larger one
- **`Palindrom.php`** — Checks whether a string or number is a palindrome
- **`Pyramid.php` / `Pyramid 2.php`** — Prints pyramid patterns using nested loops
- **OOP programs** — Python classes demonstrating encapsulation, inheritance, and more
- **HTML practicals** — Structured web pages from Semester 1 WP sessions

---

## 🚀 Getting Started

### Prerequisites

Before running any PHP practicals locally, make sure you have:

- **PHP 7.4+** installed ([Download PHP](https://www.php.net/downloads))
- A local web server environment — one of:
  - [XAMPP](https://www.apachefriends.org/)
  - [WampServer](https://sourceforge.net/projects/wampserver/)
  - [MAMP](https://www.mamp.info/)
  - Or PHP's built-in development server
- A code editor like [Visual Studio Code](https://code.visualstudio.com/)

For Python practicals, make sure **Python 3.x** is installed ([Download Python](https://www.python.org/downloads/)).

---

### 🖥️ Running PHP Practicals

#### Option A: Using XAMPP / WampServer / MAMP

1. Install and launch your server environment (Apache + PHP must be running).
2. Copy or move the cloned repository folder into the server's document root:
   - **WampServer:** `C:\wamp64\www\` or `D:\wamp64\www\`
   - **XAMPP:** `C:\xampp\htdocs\`
3. Open your browser and navigate to `http://localhost/Awesome-BscIT/`
4. Browse to any PHP file to see its output.

#### Option B: PHP Built-in Server

```bash
# Clone the repository
git clone https://github.com/ThVariableYT/Awesome-BscIT.git
cd Awesome-BscIT

# Start the built-in PHP server
php -S localhost:8080
```

Then open your browser and go to `http://localhost:8080`.

---

### 🐍 Running Python Practicals

```bash
# Navigate to the OOP or PADP folder
cd "Semester 2/OOP"

# Run any Python file
python filename.py
```

---

## ⚙️ GitHub Actions (CI/CD)

This repository uses **GitHub Actions** for automated validation:

- **PHP Syntax Validation** — Checks all `.php` files for syntax errors using `php -l`
- **HTML Validation** — Validates HTML files for well-formedness

Workflow files are located in `.github/workflows/`. Every push to `main` triggers these checks automatically.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new practicals or improve existing ones:

1. **Fork** this repository
2. **Create a new branch:**
   ```bash
   git checkout -b feature/your-practical-name
   ```
3. **Add your changes** and commit with a clear message:
   ```bash
   git commit -m "Add: Fibonacci series practical in PHP"
   ```
4. **Push** to your fork and **open a Pull Request**
5. Make sure your code is clean, commented, and functional

> Please follow the existing folder structure when adding new practicals (`Semester X / Subject /`).

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this code for educational purposes. See the [LICENSE](LICENSE) file for full details.

---

## 🙋 Author & Contact

**Jash Gandhi** — [@ThVariableYT](https://github.com/ThVariableYT)

- 🌐 Live Site: [thvariableyt.github.io/Awesome-BscIT](https://thvariableyt.github.io/Awesome-BscIT/)
- 💻 GitHub: [github.com/ThVariableYT](https://github.com/ThVariableYT)

---

*Happy coding! 🚀 Keep learning and keep building.*

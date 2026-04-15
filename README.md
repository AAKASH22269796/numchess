# ♟️ NumChess — Strategic Number Placement Game

NumChess is a **two-player strategy game** built using **Python and PyQt5**, where players take turns placing increasing numbers on a triangular board.
The winner is determined through a **unique neighbor-based scoring system**, making the game both simple and strategic.

---

## 🧠 Game Concept

NumChess is not a traditional chess game — instead, it focuses on **number placement and positional strategy**.

* Two players: **Red (R)** and **Green (G)**
* Players take turns placing numbers on empty cells
* Each player places numbers in sequence (1 → 7)
* The board fills up except for **one final empty cell**
* The winner is decided based on **neighboring values of that empty cell**

👉 This creates a mix of:

* Planning ahead
* Blocking opponent moves
* Optimizing number placement

---

## 🎮 Gameplay Rules

1. The board is triangular (5 rows)
2. Players alternate turns:

   * Red starts first
   * Then Green, and so on
3. Each move:

   * Places the next number for that player
4. After all moves:

   * One empty cell remains
   * All its neighboring cells are checked

### 🏆 Winning Logic

* Sum of Red’s numbers around the empty cell → `red_sum`
* Sum of Green’s numbers around the empty cell → `green_sum`

| Condition           | Result        |
| ------------------- | ------------- |
| red_sum < green_sum | 🔴 Red Wins   |
| green_sum < red_sum | 🟢 Green Wins |
| equal               | 🤝 Draw       |

---

## 🖥️ Features

* 🎯 Turn-based gameplay (Red vs Green)
* 🔢 Automatic number assignment
* 🎨 Interactive GUI with PyQt5
* 🟡 Highlighting of final empty cell
* 🟣 Highlighting of neighboring cells
* 🏆 Automatic winner calculation
* 🔄 "Play Again" functionality
* ⚡ Smooth and simple user experience

---

## 📁 Project Structure

```
numchess/
│── game.py        # Core game logic (board, moves, scoring)
│── ui.py          # UI rendering and interactions (PyQt5)
│── main.py        # Application entry point
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/AAKASH22269796/numchess.git
cd numchess
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```
python main.py
```

This will launch the graphical game window.

---

## 🧪 Tech Stack

* **Python** — Core programming language
* **PyQt5** — GUI framework
* **Object-Oriented Design** — Clean separation of logic and UI

---

## 🧩 Code Architecture

### 🔹 Game Logic (`game.py`)

* Handles:

  * Board creation
  * Turn management
  * Move validation
  * Neighbor detection
  * Final result calculation

### 🔹 User Interface (`ui.py`)

* Builds the triangular board layout
* Handles button clicks and UI updates
* Displays:

  * Current turn
  * Final result
  * Visual highlights

### 🔹 Entry Point (`main.py`)

* Initializes the PyQt application
* Launches the main game window

---

## 📦 Build Executable (Optional)

You can convert this into a standalone app:

```
pip install pyinstaller
pyinstaller --onefile main.py
```

Executable will be generated inside the `dist/` folder.

---

## 🚀 Future Enhancements

* 🤖 AI opponent (single-player mode)
* 🌐 Web version (HTML/CSS/JS)
* 🎨 Improved UI/UX design
* 🔊 Sound effects and animations
* 🧮 Advanced scoring variations

---

## 👨‍💻 Author

**Aakash Mahatha**

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub!

---

## 📌 Note

This project is ideal for:

* Learning **PyQt5 GUI development**
* Understanding **game logic design**
* Practicing **object-oriented programming**
* Building a **strong portfolio project**

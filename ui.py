from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from game import Game
from PyQt5.QtCore import Qt
import math

class MainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.game = Game()

        self.setWindowTitle("Number Chess")
        self.setGeometry(100, 100, 500, 600)

        self.setup_ui()

    def setup_ui(self):
        self.buttons = []

        self.label = QLabel(self)
        self.label.setStyleSheet("font-size: 18px;")
        self.label.setGeometry(100, 10, 300, 40)   # 🔥 important
        self.label.setAlignment(Qt.AlignCenter)    # 🔥 center text

        self.result_label = QLabel(self)
        self.result_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.result_label.setGeometry(100, 420, 300, 40)
        self.result_label.setAlignment(Qt.AlignCenter)

        self.play_again = QPushButton("Play Again", self)
        self.play_again.move(200, 500)
        self.play_again.clicked.connect(self.reset_game)
        self.play_again.hide()

        self.update_label()

        n = 5
        size = 60
        r = size // 2
        center_x = 250

        for i in range(n):
            row_buttons = []

            y = 50 + i * (r * math.sqrt(3))
            row_width = (i + 1) * size
            start_x = center_x - row_width // 2

            for j in range(i + 1):
                x = start_x + j * size

                btn = QPushButton("", self)
                btn.setFixedSize(size, size)

                btn.setStyleSheet("""
                    QPushButton {
                        border-radius: 30px;
                        background-color: lightgray;
                        border: 1px solid black;
                    }
                """)

                btn.move(int(x), int(y))

                btn.i = i
                btn.j = j

                btn.clicked.connect(self.handle_click)

                row_buttons.append(btn)

            self.buttons.append(row_buttons)

    def handle_click(self):
        if self.game.is_game_over():
            return

        btn = self.sender()
        i, j = btn.i, btn.j

        result = self.game.make_move(i, j)

        if result is None:
            return

        player, value = result

        btn.setText(str(value))

        if player == "R":
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 30px;
                    background-color: red;
                    color: white;
                    border: 1px solid black;
                }
                """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 30px;
                    background-color: green;
                    color: white;
                    border: 1px solid black;
                }
                """)

        if self.game.is_game_over():
            self.end_game()
        else:
            self.update_label()

    def end_game(self):
        empty, neighbors, red_sum, green_sum, winner = self.game.get_result()

        i, j = empty

        # 🟡 highlight empty node
        empty_btn = self.buttons[i][j]
        empty_btn.setStyleSheet("""
            QPushButton {
                border-radius: 30px;
                background-color: yellow;
                border: 3px solid black;
            }
        """)

        # 🟣 highlight neighbors
        for x, y in neighbors:
            btn = self.buttons[x][y]
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 30px;
                    background-color: purple;
                    color: white;
                    border: 2px solid black;
                }
            """)

        # 🏆 result text
        if winner == "R":
            text = f"Red Wins ({red_sum} vs {green_sum})"
        elif winner == "G":
            text = f"Green Wins ({green_sum} vs {red_sum})"
        else:
            text = f"Draw ({red_sum})"

        self.result_label.setText(text)
        self.label.setText("Game Over")

        self.play_again.show()  

    def update_label(self):
        player, value = self.game.get_turn()
        text = "Red " + str(value) if player == "R" else "Green " + str(value)
        self.label.setText(text)

    def reset_game(self):
        self.game.reset()
        self.result_label.setText("")
        self.play_again.hide()

        for row in self.buttons:
            for btn in row:
                btn.setText("")
                btn.setStyleSheet("""
                    QPushButton {
                        border-radius: 30px;
                        background-color: lightgray;
                        border: 1px solid black;
                    }
                """)

        self.update_label()
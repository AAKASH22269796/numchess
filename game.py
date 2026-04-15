class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [
            [None],
            [None, None],
            [None, None, None],
            [None, None, None, None],
            [None, None, None, None, None]
        ]

        self.current_player = "R"
        self.red_count = 1
        self.green_count = 1

    def make_move(self, i, j):
        if self.board[i][j] is not None:
            return None

        if self.current_player == "R":
            value = self.red_count
            self.board[i][j] = ("R", value)
            self.red_count += 1
            self.current_player = "G"
        else:
            value = self.green_count
            self.board[i][j] = ("G", value)
            self.green_count += 1
            self.current_player = "R"

        return self.board[i][j]

    def get_turn(self):
        if self.current_player == "R":
            return ("R", self.red_count)
        else:
            return ("G", self.green_count)

    def is_game_over(self):
        return self.red_count == 8 and self.green_count == 8

    def get_neighbors(self, i, j):
        neighbors = []
        n = len(self.board)

        if j - 1 >= 0:
            neighbors.append((i, j - 1))
        if j + 1 < len(self.board[i]):
            neighbors.append((i, j + 1))

        if i - 1 >= 0:
            if j - 1 >= 0:
                neighbors.append((i - 1, j - 1))
            if j < len(self.board[i - 1]):
                neighbors.append((i - 1, j))

        if i + 1 < n:
            neighbors.append((i + 1, j))
            neighbors.append((i + 1, j + 1))

        return neighbors

    def get_result(self):
        empty = None

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    empty = (i, j)

        i, j = empty
        neighbors = self.get_neighbors(i, j)

        red_sum = 0
        green_sum = 0

        for x, y in neighbors:
            player, value = self.board[x][y]
            if player == "R":
                red_sum += value
            else:
                green_sum += value

        if red_sum < green_sum:
            winner = "R"
        elif green_sum < red_sum:
            winner = "G"
        else:
            winner = "D"

        return empty, neighbors, red_sum, green_sum, winner
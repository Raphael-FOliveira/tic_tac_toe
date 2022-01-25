

class Board:

    def __init__(self):
        self.positions = [[" " for _ in range(3)] for _ in range(3)]
        self.board = f"| {self.positions[0][0]} | {self.positions[0][1]} | {self.positions[0][2]} |\n" \
                     f"-------------\n" \
                     f"| {self.positions[1][0]} | {self.positions[1][1]} | {self.positions[1][2]} |\n" \
                     f"-------------\n" \
                     f"| {self.positions[2][0]} | {self.positions[2][1]} | {self.positions[2][2]} |\n" \


    def place_x(self, row, col):
        self.positions[row-1][col-1] = "X"
        self.board = f"| {self.positions[0][0]} | {self.positions[0][1]} | {self.positions[0][2]} |\n" \
                     f"-------------\n" \
                     f"| {self.positions[1][0]} | {self.positions[1][1]} | {self.positions[1][2]} |\n" \
                     f"-------------\n" \
                     f"| {self.positions[2][0]} | {self.positions[2][1]} | {self.positions[2][2]} |\n" \


    def place_o(self, row, col):
        self.positions[row-1][col-1] = "O"
        self.board = f"| {self.positions[0][0]} | {self.positions[0][1]} | {self.positions[0][2]} |\n" \
                     f"-------------\n" \
                     f"| {self.positions[1][0]} | {self.positions[1][1]} | {self.positions[1][2]} |\n" \
                     f"-------------\n" \
                     f"| {self.positions[2][0]} | {self.positions[2][1]} | {self.positions[2][2]} |\n" \

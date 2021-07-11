import copy
import random

from figures import transpose, generate_figure


COEFFICIENT = 0.95


class Tetris:
    next = None
    current = None
    pos = None

    update_time = 1  # step per 1 second
    time = 0

    back_board = None

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.board = [[0] * width] * height

    def start(self):
        self.next = generate_figure()
        self.next_figure()

    def next_figure(self):
        self.back_board = copy.deepcopy(self.board)

        self.current = self.next
        self.next = generate_figure()

        variants = list(range(self.width - len(self.current[0])))
        random.shuffle(variants)
        for x in variants:
            pos = (x, 0)
            board = self.figure_board(self.current, pos)
            if board:
                self.pos = pos
                self.update_board(board)
                break
        else:
            pass  # TODO game over

    def figure_board(self, figure, pos):
        figure_x, figure_y = pos
        figure_length_x, figure_length_y = len(figure[0]), len(figure)

        #  checking if figure is inside of board
        if not (0 <= figure_y <= figure_y + figure_length_y <= self.height and
                0 <= figure_x <= figure_x + figure_length_x <= self.width):
            return

        board = copy.deepcopy(self.back_board)
        for y in range(figure_length_y):
            for x in range(figure_length_x):
                if figure[y][x]:
                    if board[y + figure_y][x + figure_x]:  # superimposition
                        return
                    board[y + figure_y][x + figure_x] = figure[y][x]
        return board

    def update_board(self, board):
        self.board = board

    def step(self):
        board = self.figure_board(self.current, (self.pos[0], self.pos[1] + 1))
        if board:
            self.update_board(board)
        else:
            self.next_figure()

    def rotate(self):
        figure = transpose(self.current)
        board = self.figure_board(figure, self.pos)
        if board:
            self.update_board(board)

    def update(self, delta):
        self.time += delta
        if self.time >= self.update_time:
            self.step()
            self.time = 0
            self.update_time *= COEFFICIENT

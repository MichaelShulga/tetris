import copy
import random

from figures import transposed, get_figure


LINE_COMPLETE = 100
FIGURE_DROP = 10

COEFFICIENT = 0.95


class TetrisModel:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.board = [[0] * width for _ in range(height)]

        self.next, self.current, self.pos = None, None, None

        self.update_time = 0.5  # step per 1 second
        self.time = 0

        self.back_board = None

        self.running = False
        self.pts = 0

    def reset(self):
        self.__init__(self.width, self.height)

    def start(self):
        self.running = True
        self.next = get_figure()
        self.next_figure()

    def next_figure(self):
        self.back_board = copy.deepcopy(self.board)

        self.current = self.next
        self.next = get_figure()

        variants = list(range(self.width - len(self.current[0])))
        random.shuffle(variants)
        for x in variants:
            if self.update_board(self.current, (x, 0)):
                break
        else:  # game over if can not set figure
            print("game over")
            self.running = False

    def update_board(self, figure, pos):
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

        self.board = board
        self.current = figure
        self.pos = pos

        return True

    def step(self):
        if not self.update_board(self.current, (self.pos[0], self.pos[1] + 1)):
            self.remove_full()
            self.next_figure()

            self.pts += FIGURE_DROP

    def remove_full(self):
        for line in self.board:
            if not line.count(0):
                self.board.remove(line)
                self.board.insert(0, [0] * self.width)

                self.update_time *= COEFFICIENT
                self.pts += LINE_COMPLETE

    def rotate(self):
        if self.running:
            self.update_board(transposed(self.current), self.pos)

    def move(self, x=0, y=0):
        if self.running:
            self.update_board(self.current, (self.pos[0] + x, self.pos[1] + y))

    def update(self, delta):
        if self.running:
            self.time += delta
            if self.time >= self.update_time:
                self.step()
                self.time = 0

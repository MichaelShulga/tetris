import random


figure1 = [[1, 1, 1, 1]]
figure2 = [[2, 2],
           [2, 2]]
figure3 = [[0, 3, 0],
           [3, 3, 3]]
figure4 = [[4, 4, 4],
           [4, 0, 0]]
figure5 = [[5, 0, 0],
           [5, 5, 5]]
figure6 = [[6, 6, 0],
           [0, 6, 6]]
figure7 = [[0, 7, 7],
           [7, 7, 0]]

figures = [figure1, figure2, figure3, figure4, figure5, figure6, figure7]


def transpose(matrix):
    return [[j[i] for j in matrix] for i in reversed(range(len(matrix)))]


def generate_figure():
    figure = random.choice(figures)
    for _ in range(random.randint(0, 3)):
        transpose(figure)
    return figure

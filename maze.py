from cell import Cell
from graphics import Window
from time import sleep
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x,
                 cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self.__create_cels()
        self.__break_entrance_and_exit()

    def __create_cels(self):
        for n in range(self._num_cols):
            top_level_list = []
            for m in range(self._num_rows):
                cell_to_add = Cell(self._win)
                top_level_list.append(cell_to_add)
            self._cells.append(top_level_list)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self._win is None:
            return
        left_top_x = (i * self._cell_size_x) + self._x1
        left_top_y = j * self._cell_size_y + self._y1

        right_bottom_x = left_top_x + self._cell_size_x
        right_bottom_y = left_top_y + self._cell_size_y

        self._cells[i][j].draw(left_top_x, left_top_y, right_bottom_x, right_bottom_y)
        self.__animate()

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self._num_cols - 1, self._num_rows - 1)

    def __break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])

    def __animate(self):
        self._win.redraw()
        sleep(0.05)

from cell import Cell
from graphics import Window
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x,
                 cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.__create_cels()

    def __create_cels(self):
        for n in range(self.num_cols):
            top_level_list = []
            for m in range(self.num_rows):
                cell_to_add = Cell(self.win)
                top_level_list.append(cell_to_add)
            self.cells.append(top_level_list)

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        left_top_x = (i * self.cell_size_x) + self.x1
        left_top_y = j * self.cell_size_y + self.y1

        right_bottom_x = left_top_x + self.cell_size_x
        right_bottom_y = left_top_y + self.cell_size_y

        self.cells[i][j].draw(left_top_x, left_top_y, right_bottom_x, right_bottom_y)
        self.__animate()

    def __animate(self):
        self.win.redraw()
        sleep(0.05)

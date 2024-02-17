from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

win = Window(800, 600)
test = Maze(10, 10, 5, 5, 50, 50, win)

win.wait_for_close()


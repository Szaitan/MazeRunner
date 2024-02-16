from graphics import Window, Line, Point
from cell import Cell

win = Window(800, 600)
# line = Line(Point(50, 50), Point(400, 400))
cell = Cell(win)
cell1 = Cell(win)
# win.draw_line(line, "black")
win.wait_for_close()


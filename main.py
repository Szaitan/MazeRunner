from graphics import Window, Line, Point
from cell import Cell

win = Window(800, 600)
# line = Line(Point(50, 50), Point(400, 400))
cell = Cell(win)
cell1 = Cell(win)
# win.draw_line(line, "black")
cell.draw(0, 50, 0, 50)
cell1.draw(50, 100, 50, 100)
cell.draw_move(cell1)
win.wait_for_close()


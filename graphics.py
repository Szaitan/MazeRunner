from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Runner")
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__running_window = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running_window = True
        while self.__running_window:
            self.redraw()

    def close(self):
        self.__running_window = False


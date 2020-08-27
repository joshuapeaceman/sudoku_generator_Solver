import random

from PyQt5.QtWidgets import QTableWidgetItem

from src.gui import SudokuMainWindow


class AppCtrl:
    def __init__(self):
        self._mainWindow = None
        self._sudoku = None

        self.initiate_mainWindow()
        self.connect_gui_element_interactions()

    def initiate_mainWindow(self):
        self._mainWindow = SudokuMainWindow.SudokuMainWindow()
        self._mainWindow.show()

    def connect_gui_element_interactions(self):
        self._mainWindow.pB_create_new.clicked.connect(lambda: self.build_sudoku(3, 17))

    def build_sudoku(self, m, min_filled_fields):
        n = m ** 2
        board = [[None for _ in range(n)] for _ in range(n)]

        def backtracking(c=0):
            i, j = divmod(c, n)
            i0, j0 = i - i % m, j - j % m  # Origin of mxm block
            for x in range(1, n + 1):
                number = random.randint(1, n)
                if (number not in board[i]  # row
                        and all(row[j] != number for row in board)  # column
                        and all(number not in row[j0:j0 + m]  # block
                                for row in board[i0:i])):
                    board[i][j] = number
                    if c + 1 >= n ** 2 or backtracking(
                            c + 1):  # return board when done: when c+ 1 >= matrix or the result of search() is not None
                        return board
            # only backtrack after having test all possible numbers, not every after every number
            else:
                board[i][j] = None
                return None

        self._sudoku = backtracking()
        self.fill_tableWidget_with_sudoku_data(m)

    def fill_tableWidget_with_sudoku_data(self, m):
        n = m ** 2
        self._mainWindow.sudokuTable.setRowCount(n)
        self._mainWindow.sudokuTable.setColumnCount(n)
        # self._mainWindow.sudokuTable.verticalHeader.setVisible(False)

        for row, row_data in enumerate(self._sudoku):
            for column, column_data in enumerate(row_data):
                self._mainWindow.sudokuTable.setItem(row, column, QTableWidgetItem(str(column_data)))

    def generate_number_and_check_legitimacy(self):
        pass

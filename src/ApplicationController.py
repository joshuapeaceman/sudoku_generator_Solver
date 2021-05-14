import random
from PyQt5 import QtWidgets
from datetime import datetime
import timeit

from src.gui import SudokuMainWindow
from src import Statistics

class AppCtrl:
    def __init__(self):
        self.mainWindow = None
        self.sudoku = None


        self.initiate_mainWindow()
        self.connect_gui_element_interactions()
        self.statistics_modul = Statistics.Statistics(self)

    def initiate_mainWindow(self):
        self.mainWindow = SudokuMainWindow.SudokuMainWindow()
        self.mainWindow.show()

    def connect_gui_element_interactions(self):
        self.mainWindow.pB_create_new.clicked.connect(lambda: self.build_sudoku(3, 30))

    def build_sudoku(self, m, difficulty):
        self.statistics_modul.game_creation_start_time = timeit.default_timer()
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

        self.sudoku = backtracking()
        self.fill_tableWidget_with_sudoku_data(difficulty)

    def fill_tableWidget_with_sudoku_data(self, difficulty):
        self.clear_sudoku()
        self.statistics_modul.empty_fields_cnt = 0
        for row, row_data in enumerate(self.sudoku):
            for column, column_data in enumerate(row_data):
                if not random.randint(1, 81) <= difficulty:
                    self.mainWindow.findChild(QtWidgets.QLineEdit, self.create_lineEdit_name(column, row)).setText(
                        str(column_data))
                else:
                    self.statistics_modul.empty_fields_cnt += 1

        self.statistics_modul.game_creation_end_time = timeit.default_timer()
        self.statistics_modul.how_many_fields_are_empty()
        self.statistics_modul.calculate_game_creation_time()
        self.statistics_modul.game_start_time = datetime.now()

    def clear_sudoku(self):
        for row, row_data in enumerate(self.sudoku):
            for column, column_data in enumerate(row_data):
                self.mainWindow.findChild(QtWidgets.QLineEdit, self.create_lineEdit_name(column, row)).setText('')

    def create_lineEdit_name(self, column, row):
        return 's' + str(row + 1) + str(column + 1)

    def generate_number_and_check_legitimacy(self):
        pass

import os

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from src.helpers import BasePath

class SudokuMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(BasePath.BasePath().get_base_path(),'src', 'gui', 'SudokuGeneratorSolverMainWindow.ui'), self)
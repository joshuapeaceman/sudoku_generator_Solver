import sys
import traceback

from PyQt5 import QtWidgets
from src import ApplicationController


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        appCtrl = ApplicationController.AppCtrl()

        sys.exit(app.exec_())
    except:
        traceback.print_exc()
import sys
import traceback

if __name__ == "__main__":
    try:
        #app = QtWidgets.QApplication(sys.argv)
        print('Hello World')

        # sys.exit(app.exec_())
    except:
        traceback.print_exc()
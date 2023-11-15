import sys
from PyQt5 import (
    QtWidgets,
    QtCore
)

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    try:
        css_file = QtCore.QFile("format.css")
        if css_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            style = QtCore.QTextStream(css_file).readAll()
            css_file.close()

        app.setStyleSheet(style)
    except:
        pass
    
    mainWindow = MainWindow()
    try:
        mainWindow.show()
    except:
        pass
    sys.exit(app.exec_())

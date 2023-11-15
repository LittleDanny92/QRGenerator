from PyQt5 import QtWidgets

def center(geometry):
    monitor_center = QtWidgets.QDesktopWidget().availableGeometry().center()
    geometry.moveCenter(monitor_center)
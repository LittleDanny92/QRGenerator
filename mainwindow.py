from PyQt5 import (
    QtWidgets,
    QtCore
)
from center import center

from simpleqrcode import SimpleQrcode

class MainWindow(QtWidgets.QMainWindow):

    colors = {
        "Black": "#000000", 
        "White": "#FFFFFF",
        "Charcoal": "#34282C",
        "Ash Gray": "#666362",
        "Blue": "#0000FF",
        "Navy": "#000080",
        "Midday Blue": "#3BB9FF",
        "Green": "#008000",
        "Deep Emerald Green": "#046307",
        "Red": "#FF0000",
        "Gaprefruit": "#DC381F"
    }

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRCodeGenerator")
        self.setFixedSize(500,240)
        center(self.frameGeometry())

        self.init_gui()

    def init_gui(self):
        
        main = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout()
        main.setLayout(grid)
        self.setCentralWidget(main)

        grid.setSpacing(15)

        self.qr_data_label = QtWidgets.QLabel("Text to convert:")
        grid.addWidget(self.qr_data_label, 0,0,1,3, QtCore.Qt.AlignLeft)

        self.qr_data_edit = QtWidgets.QLineEdit()
        self.qr_data_edit.setMaxLength(200)
        self.qr_data_edit.setFixedHeight(40)
        grid.addWidget(self.qr_data_edit, 0,2,1,3)

        self.qr_size_label = QtWidgets.QLabel("Size of QR code:")
        grid.addWidget(self.qr_size_label, 1,0,1,3, QtCore.Qt.AlignLeft)

        self.qr_size_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.qr_size_slider.setMinimum(8)
        self.qr_size_slider.setMaximum(16)
        self.qr_size_slider.setValue(12)
        self.qr_size_slider.setSingleStep(2)
        grid.addWidget(self.qr_size_slider, 1,2,1,3)

        self.qr_color_label = QtWidgets.QLabel("Color of QR:")
        grid.addWidget(self.qr_color_label, 2,0,1,3, QtCore.Qt.AlignLeft)

        self.qr_color_combobox = QtWidgets.QComboBox()
        self.qr_color_combobox.addItems([color for color in self.colors])
        grid.addWidget(self.qr_color_combobox, 2,2,1,3)

        self.qr_bgcolor_label = QtWidgets.QLabel("Color of background:")
        grid.addWidget(self.qr_bgcolor_label, 3,0, QtCore.Qt.AlignLeft)

        self.qr_bgcolor_combobox = QtWidgets.QComboBox()
        self.qr_bgcolor_combobox.addItems([color for color in self.colors])
        grid.addWidget(self.qr_bgcolor_combobox, 3,2,1,3)

        self.qr_create_button = QtWidgets.QPushButton("Create QR")
        self.qr_create_button.setFixedSize(100,40)
        grid.addWidget(self.qr_create_button, 4,0,1,2, QtCore.Qt.AlignRight)

        self.form_reset_button = QtWidgets.QPushButton("Reset the form")
        self.form_reset_button.setFixedSize(100,40)
        grid.addWidget(self.form_reset_button, 4,2,1,2, QtCore.Qt.AlignRight)

        self.qr_create_button.clicked.connect(self.execute_creating_process)
        self.form_reset_button.clicked.connect(self.reset_form)

        self.error_msg_box = QtWidgets.QMessageBox()
        self.error_msg_box.setWindowTitle("Error")
        self.error_msg_box.setText("The creation of QR code failed.")
        self.error_msg_box.setIcon(QtWidgets.QMessageBox.Warning)

        self.info_msg_box = QtWidgets.QMessageBox()
        self.info_msg_box.setWindowTitle("Information")
        self.info_msg_box.setIcon(QtWidgets.QMessageBox.Information)

    def execute_creating_process(self):
        if self.qr_color_combobox.currentText() != self.qr_bgcolor_combobox.currentText():
            try:
                qr = SimpleQrcode(self.qr_data_edit.text(), box_size = self.qr_size_slider.value(),
                                  color = self.colors[self.qr_color_combobox.currentText()],
                                  bgcolor = self.colors[self.qr_bgcolor_combobox.currentText()])
                qr_image = qr.create_qr()
                self.save_qr(qr_image)
            except:
                self.error_msg_box.exec()
            else:
                self.info_msg_box.setText("QR code is ready to use.")
                self.info_msg_box.exec()
        else:
            self.info_msg_box.setText("The color of QR must be different from background color.")
            self.info_msg_box.exec()
    
    def save_qr(self, qr_image):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self,"Save PNG File", "", "Images (*.png);; All Files (*)")
        if file_path:
            qr_image.save(file_path)

    def reset_form(self):
        self.qr_data_edit.clear()
        self.qr_size_slider.setValue(12)

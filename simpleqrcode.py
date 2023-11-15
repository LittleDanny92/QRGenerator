import qrcode

class SimpleQrcode:
    def __init__(self, data, box_size = 14, color = "black", bgcolor = "white"):
        self._data = data
        self._box_size = box_size
        self._color = color
        self._bgcolor = bgcolor

    @property
    def data(self): return self._data

    @property
    def box_size(self): return self._box_size
    
    @property
    def color(self): return self._color

    @property
    def bgcolor(self): return self._bgcolor

    def create_qr(self):
        qr = qrcode.QRCode(version = 1, box_size = self.box_size, border = 8)

        qr.add_data(self.data)
        qr.make(fit=True)

        return qr.make_image(fill_color = self.color, back_color = self.bgcolor)

    def __str__(self):
        return f"Inserted data: {self._data},/n color: {self._color}, /n background color: {self._bgcolor}"
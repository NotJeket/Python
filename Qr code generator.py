#install using pip install in terminal.
import qrcode

py_qrcode = qrcode.make ("https://www.google.com/")
py_qrcode.save ("googleQR.jpg")
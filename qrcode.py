import pyqrcode
import png
from pyqrcode import QRCode

website = "https://forms.gle/whH2ptytYoSMyjgG8"

url = pyqrcode.create(website)

# url.svg('dsqr.svg', scale=8)
url.png('dsqr.png', scale=16)
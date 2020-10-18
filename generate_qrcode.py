import pyqrcode
import png
from pyqrcode import QRCode

s = "(website_name)"

url = pyqrcode.create(s)

url.svg("(file_name_save).svg",scale = 8)
url.png('(file_name_save).png',scale = 6)

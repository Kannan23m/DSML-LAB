import pyqrcode
from pyqrcode import QRCode
s = input("enter your url")
myqr = input("enter your filename")
url = pyqrcode.create(s)
url.svg(myqr+".svg",scale=8)
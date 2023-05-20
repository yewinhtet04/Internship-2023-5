import pytesseract as pss
pss.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img=Image.open('images/bay3.jpg')
text=pss.image_to_string(img)
print(text)
want=['Transaction Time','Transfer To','Amount']
z=text[text.find(want[0]):]
x=text[text.find(want[1]):]
y=text[text.find(want[2]):]
z=z[:z.find('\n')]
x=x[:x.find('\n')]
y=y[:y.find('\n')]
data={want[0]:z.replace(want[0],''),want[1]:x.replace(want[1],''),want[2]:y.replace(want[2],'')}
print(data)
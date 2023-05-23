import json

import pytesseract as pss
pss.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import json

img=Image.open('images/bay6.jpg')
text=pss.image_to_string(img)
print(text)

want=['Transaction Time','Transaction No.','Transaction Type','Transfer To','Amount','Notes']
data={}
for i in want:
    z=text[text.find(i):]
    z=z[:z.find('\n')]
    data.update({i:z.replace(i,'')})

print(json.dumps(data,indent=4))
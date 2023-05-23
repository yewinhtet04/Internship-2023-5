from django.shortcuts import render,redirect

import pytesseract as pss
pss.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
# Create your views here.
def upload(request):
    return render(request,'upload.html')

def index(request):
    return redirect('image/upload')

def text(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image = Image.open(image)
        text=pss.image_to_string(image)
        want=['Transaction Time','Transaction No.','Transaction Type','Transfer To','Amount','Notes']
        data={}
        for i in want:
            z=text[text.find(i):]
            z=z[:z.find('\n')]
            data.update({i:z.replace(i,'')})
        return render(request,'result.html',{'data':data})
    return redirect('/image/upload')
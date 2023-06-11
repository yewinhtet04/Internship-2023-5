import json
import re, os
import pytesseract as pss
from PIL import Image

def findd(aa):
    for i in range(len(aa)):
        if re.search('Su[a-z]+ful', aa[i]):       return i
    else:
        return -1


def extract(img, z):
    pss.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
    m_data = pss.image_to_string(img)
    m_data = m_data.split('\n')

    want = [['Date', 'Transaction Id', 'Type', 'Name', 'Amount'],
            ['Name', 'Phone', 'Type', 'Amount', 'Date', 'Transaction Id']][z]
    in_m = [['Transaction Time', 'Transaction ID', 'Transaction Type', 'Transfer To', 'Amount'],
            ['-', '-', 'Type', 'Amount', 'Date', 'Transaction ID']][z]
    regrex = [['[0-9]{2}\D[0-9]{2}\D[0-9]{4}\D[0-9]{2}\D[0-9]{2}\D[0-9]{2}',
               '[0-9]{10}[0-9]+',
               '([A-Za-z]+\s*)+',
               '([A-Z][a-zA-Z]+\s*)+',
               '\W[0-9]([0-9]|\W)*[0-9]+ [A-Za-z]*', ],
              ['([A-Z][a-zA-Z]+\s*)+',
               '(9|09)([0-9]{10}|[0-9]{9})',
               '([A-Za-z]+\s*)+',
               '[0-9][0-9]+ [A-Za-z]*',
               '[0-9]+( |.)[A-Z][a-z]+( |.)[0-9]+',
               '[0-9][0-9]+']][z]
    # print(z,regrex)
    cond = [[lambda a, b: 'Transaction' in a or 'Time' in a or re.search(regrex[b], a),
             lambda a, b: 'Transaction' in a or 'No' in a or re.search(regrex[b], a),
             lambda a, b: 'Type' in a or re.search(regrex[b], a),
             lambda a, b: 'Transfer' in a or re.search(regrex[b], a),
             lambda a, b: 'Amount' in a or re.search(regrex[b], a), ],
            [lambda a, b: re.search(regrex[b], a),
             lambda a, b: re.search(regrex[b], a),
             lambda a, b: 'Wave' in a or 'Type' in a or re.search(regrex[b], a),
             lambda a, b: 'Amount' in a or re.search(regrex[b], a),
             lambda a, b: 'Date' in a or re.search(regrex[b], a),
             lambda a, b: 'Transaction' in a or 'ID' in a or re.search(regrex[b], a)]][z]
    want_id = 0
    m_data = m_data[findd(m_data) + 1:]
    data = {}
    for d in m_data:
        if want_id < len(want) and cond[want_id](d, want_id):
            ss = re.search(regrex[want_id], d.replace(in_m[want_id], '').strip())
            if ss:   data.update({want[want_id]: ss[0]});
            if z == 0 and want_id == 3:
                pp = re.search('\W+[0-9]+\W*', d)
                if pp: data.update({'Phone': pp[0].strip()})
            want_id += 1
    return data


def extract_data(image):
    #image=Image.open(img)
    data = extract(image, 0)
    if ("Date" not in data or "Transaction Id" not in data or 'Amount' not in data or 'Name' not in data):
        data = extract(image, 1)
    if "Date" not in data or "Transaction Id" not in data or 'Amount' not in data or 'Name' not in data:
        return None
    return data

#print(extract_data('payment_images/bay4.jpg'))
'''
print(extract_data('images/wave2.jpg'))

for path in os.listdir('images/'):
    print(path)
    print(extract_data('images/'+path))
'''
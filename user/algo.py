import json
def find(data:dict,mail:str):
    for k,v in data.items():
        if v['email']==mail:return v
    else: return False
def exist(data,mail):
    for k,v in data.items():
        if v['email']==mail : return True
    return False
'''
f = open('../user_data.json')
a_data = json.load(f)
print(exist(a_data,'yewinhtet04@gmail.com'))
'''
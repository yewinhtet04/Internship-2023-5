a = ['htoo', 'htto']


def compare_str(str1, str2):
    for i in range(len(str1)):
        print(str1[i],str2[i])
        if str1[i]<str2[i]: return False
        elif str1[i] > str2[i]: return True


def index(aa: list, num):
    for i in range(len(aa)):
        if compare_str(aa[i], num):   return i
    print('len')
    return len(aa)

def linear_search(aa,num):
    for i in range(len(aa)):
        if aa[i]==num:return aa[i]
    return None
num = 'htoo'
print(linear_search(a,num))
idx = index(a, num)
a = a[:idx] + [num] + a[idx:]
print(a)

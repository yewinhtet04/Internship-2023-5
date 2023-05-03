import random
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        self.left = None
        self.right = None
        self.store = None


def tree_data():
    aa = []
    for i in range(97, 123):
        aa.append(chr(i))
    return aa


def sec_tree_data():
    aa = []
    for i in range(1, 50):
        aa.append(i)
    return aa


def insert_tree_data(node: Node, data: list):
    if len(data) > 0:
        mid = len(data) // 2
        node.data = data[mid]
        if len(data[:mid]) > 0:
            node.left = Node()
            insert_tree_data(node.left, data[:mid])
        if len(data[mid + 1:]) > 0:
            node.right = Node()
            insert_tree_data(node.right, data[mid + 1:])

count=0
all_data={}
def printting(tree: Node):
    global count
    count+=1
    if tree:
        printting(tree.left)
        printting_sec(tree.link)
        printting(tree.right)
def printting_sec(tree: Node):
    global count
    count+=1
    if tree:
        printting_sec(tree.left)
        if tree.store:
            for t in tree.store:
                count+=1
                all_data.update({len(all_data):t})
        printting_sec(tree.right)


def create_tree():
    t_data = tree_data()
    # print(t_data)
    tree = Node()
    insert_tree_data(tree, t_data)
    # print(t_data)
    return tree


def create_sec_tree():
    t_data = sec_tree_data()
    # print(t_data)
    tree = Node()
    insert_tree_data(tree, t_data)
    # print(t_data)
    return tree


def insert_data(node: Node, name: str):
    if node.data == name[0]:
        if not node.link: node.link = create_sec_tree()
        insert_sec_data(node.link, name)
    elif node.data < name[0]:
        insert_data(node.right, name)
    else:
        insert_data(node.left, name)


def insert_sec_data(node: Node, name: str):
    if node.data == len(name):
        if not node.store: node.store = []
        idx = index(node.store, name)
        node.store = node.store[:idx] + [name] + node.store[idx:]
        #print(node.store)
    elif node.data < len(name):
        insert_sec_data(node.right, name)
    else:
        insert_sec_data(node.left, name)


def compare_str(str1, str2):
    for i in range(len(str1)):
        #print(str1[i], str2[i])
        if str1[i] < str2[i]:
            return False
        elif str1[i] > str2[i]:
            return True


def index(aa: list, num):
    for i in range(len(aa)):
        if compare_str(aa[i], num):   return i
    #print('len')
    return len(aa)


def search_data(node: Node, name: str):
    if node.data == name[0]:
        if not node.link: return None
        return search_sec_data(node.link, name)
    elif node.data < name[0]:
        return search_data(node.right, name)
    else:
        return search_data(node.left, name)


def search_sec_data(node: Node, name: str):
    if node.data == len(name):
        if not node.store: return None
        print(node.store)
        return linear_search(node.store, name)
    elif node.data < len(name):
        return search_sec_data(node.right, name)
    else:
        return search_sec_data(node.left, name)


def linear_search(aa, num):
    for i in range(len(aa)):
        if aa[i] == num: return aa[i]
    return None

def random_email():
    length=random.randrange(4,40)
    em=''
    for _ in range(length):
        em+=chr(random.randrange(97,123))
    return em

tree = create_tree()
for _ in range(1000):
    insert_data(tree,random_email())
count = 0
all_data = {}
printting(tree)
print(all_data)
print(count)
'''
name = input('Enter name:')
while name:
    insert_data(tree, name)
    name = input('Enter name:')
    # printting(tree)
name = input('Search name:')
print(search_data(tree, name))
'''
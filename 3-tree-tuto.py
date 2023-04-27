class Node:
    def __init__(self):
        self.data=None
        self.link=None
        self.left=None
        self.right=None
        self.store=None

def tree_data():
    aa=[]
    for i in range(97,123):
        aa.append(chr(i))
    return aa
def sec_tree_data():
    aa=[]
    for i in range(1,50):
        aa.append(i)
    return aa

def insert_tree_data(node:Node,data:list):
    if len(data)>0:
        mid=len(data)//2
        node.data=data[mid]
        if len(data[:mid])>0:
            node.left=Node()
            insert_tree_data(node.left,data[:mid])
        if len(data[mid+1:])>0:
            node.right=Node()
            insert_tree_data(node.right,data[mid+1:])

def printting(tree:Node):
    if tree:
        print(tree.data)
        printting(tree.left)
        printting(tree.right)
def create_tree():
    t_data=tree_data()
    print(t_data)
    tree=Node()
    insert_tree_data(tree,t_data)
    print(t_data)
    return tree

def create_sec_tree():
    t_data=sec_tree_data()
    print(t_data)
    tree=Node()
    insert_tree_data(tree,t_data)
    print(t_data)
    return tree


def insert_data(node:Node,name:str):
    if node.data==name[0]:
        if not node.link: node.link=create_sec_tree()
        insert_sec_data(node.link,name)
    elif node.data<name[0]:
        insert_data(node.right,name)
    else:
        insert_data(node.left,name)

def insert_sec_data(node:Node,name:str):
    if node.data==len(name):
        if not node.store: node.store=[]
        node.store.append(name)
    elif node.data<len(name):
        insert_sec_data(node.right,name)
    else:
        insert_sec_data(node.left,name)

tree=create_tree()
name=input('Enter name:')
insert_data(tree,name)
name=input('Enter name:')
insert_data(tree,name)
printting(tree)



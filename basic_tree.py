class Node:
    def __init__(self):
        self.data = None
        self.title = None
        self.link = None
        self.left = None
        self.right = None

    def insert_data(self, data):
        self.data = data


def insert(data: list, tree: Node):
    if len(data) > 0:
        mix = len(data) // 2
        # if tree==None :tree=Node()
        tree.title = data[mix]
        # print(data,mix,data[:mix],data[mix+1:])
        if len(data[:mix]) > 0:
            tree.left = Node()
            insert(data[:mix], tree.left)
        if len(data[mix + 1:]) > 0:
            tree.right = Node()
            insert(data[mix + 1:], tree.right)


def print_data(node):
    if node is not None:
        print_data(node.left)
        print(node.title)
        print_data(node.right)

def tree_alphabet():
    alphabet = ['.','@','_']
    for i in range(48, 58):
        alphabet.append(chr(i))
    for i in range(97, 123):
        alphabet.append(chr(i))
    alphabet.sort()
    return alphabet

def create_tree():
    alphabet=tree_alphabet()
    nood = Node()
    insert(alphabet, nood)
    return nood

def create_tree_node():
    node = Node()
    alphabet=tree_alphabet()
    node.title=alphabet[len(alphabet)//2]
    return node
    # print('wjkdfj',nood.data,nood.left.data,nood.left.left.data,nood.left.left.left.data)

    # print_data(nood)
trr=create_tree()
#print_data(trr)
print(int('a'))
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def insert_data(self, data):
        self.data = data


def insert(data: list, tree: Node):
    if len(data) > 0:
        mix = len(data) // 2
        # if tree==None :tree=Node()
        tree.insert_data(data[mix])
        # print(data,mix,data[:mix],data[mix+1:])
        if len(data[:mix]) > 0: tree.left = Node();insert(data[:mix], tree.left)
        if len(data[mix + 1:]) > 0: tree.right = Node();insert(data[mix + 1:], tree.right)


def print_data(node):
    if node != None:
        print_data(node.left)
        print(node.data)
        print_data(node.right)


alphabet = []
for i in range(97, 123):
    alphabet.append({'key': chr(i), 'value': i})
nood = Node()
insert(alphabet, nood)
# print('wjkdfj',nood.data,nood.left.data,nood.left.left.data,nood.left.left.left.data)

print_data(nood)

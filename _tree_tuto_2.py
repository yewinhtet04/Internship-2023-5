
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

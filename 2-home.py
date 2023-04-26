import basic_tree

tree = None
count = 0


def findneighbour(title, lr, trr=basic_tree.create_tree()):
    #print(trr.title,title)
    if trr.title == title:return trr.right.title if lr else trr.left.title
    if trr.title < title: return findneighbour(title, lr, trr.right)
    if trr.title > title: return findneighbour(title, lr, trr.left)


def insert_data(tree, info, index=0):
    #print(tree.title,info['mail'],index)
    if index >= len(info['mail']):
        #print('Added data below')
        tree.data = info
    else:
        # print(tree.data,tree.title, index,mail[index])
        # print(info['mail'][index],type(tree.title))
        if tree.title and info['mail'][index] > tree.title:
            #print('aaa',tree.right)
            if not (tree.right):
                #print('hhhh')
                tree.right = basic_tree.Node()
                tree.right.title = findneighbour(tree.title, 1)
            #print('go right',tree.right,tree.right.title)
            insert_data(tree.right, info, index)
        elif tree.title and info['mail'][index] < tree.title:
            if not (tree.left):
                tree.left = basic_tree.Node()
                tree.left.title = findneighbour(tree.title, 0)
            #print('go left',tree.left,tree.left.title)
            insert_data(tree.left, info, index)
        elif tree.title and info['mail'][index] == tree.title:
            if len(info['mail']) == index + 1:
                tree.data = info
            else:
                if not (tree.link): tree.link = basic_tree.create_tree_node()
                insert_data(tree.link, info, index + 1)
        else:
            print('Bla', tree, tree.title)


def get_data(tree, mail, index=0):
    global count
    count += 1
    # print(tree.title,mail,index)
    if index >= len(mail):
        print('Added data below')
        return tree.data
    else:
        if tree.title and mail[index] > tree.title and tree.right:
            return get_data(tree.right, mail, index)
        elif tree.title and mail[index] < tree.title and tree.left:
            return get_data(tree.left, mail, index)
        elif tree.title and mail[index] == tree.title:
            if len(mail) == index + 1:
                return tree.data
            else:
                if not (tree.link): tree.link = basic_tree.create_tree_node()
                return get_data(tree.link, mail, index + 1)
        else:
            return None


import re


def valid_mail_format(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, s):
        return True
    return False


def loop(ss, ind, trr=basic_tree.create_tree_node()):
    ans = input(ss)
    if ind == 1:
        while not ans.isalpha():
            ans = input('Invalid format! ' + ss)
    elif ind == 2:
        while not valid_mail_format(ans):
            ans = input('Invalid mail format! ' + ss)
        while get_data(trr, ans):
            ans = input('Email Already exist! ' + ss)
    else:
        while not ans.isnumeric():
            ans = input('Invalid format! ' + ss)
    return ans


def request_info(mail):
    name = loop('Enter your name:', 1)  # check alpha
    password = input('Enter your password:')
    address = input('Enter your address:')
    ph_no = loop('Enter your phone number:', 0)  # check num
    data = {'mail': mail, 'name': name, 'password': password, 'address': address, 'phone': ph_no}
    return data


def print_all(tree):
    global count
    count += 1
    # print(tree.title)
    if tree.data is not None:   print(tree.data)
    if tree.left:   print_all(tree.left)
    if tree.right:  print_all(tree.right)
    if tree.link:   print_all(tree.link)


while True:
    choose = input('Enter 1 for retrieve user\nEnter 0 for print all user\nEnter any key for create user\n>>>')
    if choose == '0':
        if not tree:   tree = basic_tree.create_tree_node()
        count = 0;
        print_all(tree);
        print(count)

    elif choose == '1':
        if not tree:   tree = basic_tree.create_tree_node()
        mail = input('Enter your email:')
        count = 0
        ans = get_data(tree, mail)
        print(ans if ans else 'NO EMAIL FOUND!')
        print(count)
    else:
        if not tree:   tree = basic_tree.create_tree_node()
        mail = loop('Enter email:', 2, tree)  # mail
        info = request_info(mail)
        insert_data(tree, info)

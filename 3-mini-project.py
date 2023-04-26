import json
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def get_data(mail):
    name = input('Enter your name:')
    password = input('Enter your password:')
    address = input('Enter your address:')
    ph_no = input('Enter your phone number:')
    data = {'mail': mail, 'name': name, 'password': password, 'address': address, 'phone': ph_no}
    return data


def check_mail(ll, mail):
    pointer = ll.head
    while pointer:
        if mail in pointer.data['mail']:
            return False
        pointer = pointer.next
    return True


if __name__ == '__main__':
    Linkedlist = LinkedList()
    while True:
        mail = input('Create an email:')
        while not (check_mail(Linkedlist, mail)):
            mail = input('Invalid email address! Reenter email Address:')
        #mail += '@yewin.com'
        print('Your email address is', mail)
        print('To complete setup, Enter the following.')
        node = Node(get_data(mail))
        # Add to linked-list
        if Linkedlist.head:
            pointer = Linkedlist.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
        else:
            Linkedlist.head = node
        # ------------------------
        print('Create email successfully.')
        # Print Data
        pointer = Linkedlist.head
        all_data = {}
        while pointer:
            all_data.update({len(all_data): pointer.data})
            pointer = pointer.next
        print(json.dumps(all_data,indent=2))

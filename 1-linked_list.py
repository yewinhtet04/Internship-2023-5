class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None




if __name__ == '__main__':
    Linkedlist = LinkedList()
    one = Node(9)
    two = Node(8)
    three = Node(6)
    Linkedlist.head = one
    one.next = two
    two.next = three
    four=Node(5)
    five=Node(3)
    three.next=four
    four.next=five

    pointer = Linkedlist.head
    while pointer is not None:
        print(pointer.data)
        pointer = pointer.next


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def contains(self, value):
        lastbox = self.head
        while lastbox is not None:
            if value == lastbox.value:
                return True
            lastbox = lastbox.next
        return False
            

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

    def remove_node(self, value):
        if self.is_empty():
            return

        last_node = current = self.head

        if value == current.value:
            self.head = current.next
            current = None
            return

        while current is not None:
            if value == current.value:
                last_node.next = current.next
                current = None
                return
            last_node = current
            current = current.next

    def is_empty(self):
        return self.head is None


ll = LinkedList()

ll.add_first(10)
ll.add_first(20)
ll.add_first(30)
ll.add_end(6)

print(ll.contains(10))
print(ll.contains(-5))
ll.print_list()

ll.remove_node(10)
ll.print_list()
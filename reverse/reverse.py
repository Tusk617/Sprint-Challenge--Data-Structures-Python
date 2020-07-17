class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None or self.head.next_node is None:
            return

        self.prev = None
        self.node = node
        # current = self.head

        while self.node:
            nextelement = self.node.next_node
            self.node.next_node = prev
            self.prev = self.node
            self.node = nextelement
        self.node = self.prev
        # self.prev = None
        # current = self.head

        # while current:
        #     temp = current.next_node
        #     current.next = self.prev
        #     self.prev = current
        #     current = temp
        
        # return self.prev
            
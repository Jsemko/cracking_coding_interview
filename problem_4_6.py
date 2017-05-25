EXAMPLE_LIST = sorted([1,4,5,9,-2,3,19,50,-20,6,100,150])

class Node(object):

    def __init__(self, value):

        self.parent = None
        self.value = value
        self.left = None
        self.right = None

    def __contains__(self, value):
        if self.value == value:
            return True
        elif value > self.value and self.right:
            return value in self.right
        elif value < self.value and self.left:
            return value in self.left
        return False

    def print_in_order_traversal(self):

        if self.left:
            self.left.print_in_order_traversal()

        print(self.value)

        if self.right:
            self.right.print_in_order_traversal()

        return

    def in_order_traversal(self):

        elements = []

        if self.left:
            elements.extend(self.left.in_order_traversal())

        elements.append(self.value)

        if self.right:
            elements.extend(self.right.in_order_traversal())

        return elements

    def insert(self, n):

        if self.value > n:
            if self.left:
                self.left.insert(n)
            else:
                self.left = Node(n)
            return
        if self.value < n:
            if self.right:
                self.right.insert(n)
            else:
                self.right = Node(n)
            return
        return

    def successor(self):

        if self.right:

            node = self.right

            while node.left:
                node = node.left
            return node

        node = self
        while node.parent:
            if node.parent.value > node.value:
                return node.parent
            node = node.parent

        return None

    def find(self, n):

        if self.value == n:
            return self

        if n < self.value:
            if self.left:
                return self.left.find(n)
            return None

        else:

            if self.right:
                return self.right.find(n)
            return None

def build_bst(sorted_list):

    if not sorted_list:
        return None

    mid_index = len(sorted_list) // 2

    mid_node = Node(sorted_list[mid_index])
    mid_node.left = build_bst(sorted_list[:mid_index])
    if mid_node.left:
        mid_node.left.parent = mid_node
    mid_node.right = build_bst(sorted_list[mid_index+1:])
    if mid_node.right:
        mid_node.right.parent = mid_node

    return mid_node



bst = build_bst(EXAMPLE_LIST)

print(bst.in_order_traversal())

start = bst.find(-20)
print(start)
print(start.successor())

while start.successor():
    print(start.value, ' ----> ', start.successor().value)
    start = start.successor()



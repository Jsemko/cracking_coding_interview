EXAMPLE_LIST = sorted([1,4,5,9,-2,3,19,50,-20,6,100,150])

class Node(object):

    def __init__(self, value):

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

def build_bst(sorted_list):

    if not sorted_list:
        return None

    mid_index = len(sorted_list) // 2

    mid_node = Node(sorted_list[mid_index])
    mid_node.left = build_bst(sorted_list[:mid_index])
    mid_node.right = build_bst(sorted_list[mid_index+1:])

    return mid_node

bst = build_bst(EXAMPLE_LIST)

print(bst.value)

print(6 in bst)
print(7 in bst)
print(150 in bst)
print(-20 in bst)

bst.print_in_order_traversal()

print(bst.in_order_traversal())

OTHER_LIST = sorted([4,7])

bst = build_bst(OTHER_LIST)

print(bst.value)
print(bst.left.value)

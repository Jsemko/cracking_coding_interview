EXAMPLE_LIST = sorted([1,4,5,9,-2,3,19,50,-20,6,100,150])
NONEXAMPLE_LIST = [1,4,5,9,-2,3,19,50,-20,6,100,150]

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

def build_bst(sorted_list):

    if not sorted_list:
        return None

    mid_index = len(sorted_list) // 2

    mid_node = Node(sorted_list[mid_index])
    mid_node.left = build_bst(sorted_list[:mid_index])
    mid_node.right = build_bst(sorted_list[mid_index+1:])

    return mid_node


def check_bst(bst):

    if bst.left:
        if bst.left.value > bst.value:
            return False
        if not check_bst(bst.left):
            return False

    if bst.right:
        if bst.right.value < bst.value:
            return False
        if not check_bst(bst.right):
            return False

    return True


bst_good = build_bst(EXAMPLE_LIST)
bst_bad = build_bst(NONEXAMPLE_LIST)

print('good one:', check_bst(bst_good))
print('bad one:', check_bst(bst_bad))

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

def check_height(node):
    if node is None:
        return 0
    return 1 + max(check_height(node.left), check_height(node.right))

def silly_check_balance(bst):
    if abs(check_height(bst.left) - check_height(bst.right)) > 1:
        return False
    if bst.left:
        if not silly_check_balance(bst.left):
            return False
    if bst.right:
        if not silly_check_balance(bst.left):
            return False
    return True

def smart_check_balance(bst):
    this_level = [bst]

    still_good = True

    while still_good and this_level:

        next_level = []

        for node in this_level:

            if node.left:
                next_level.append(node.left)
            else:
                still_good = False

            if node.right:
                next_level.append(node.right)
            else:
                still_good = False

        this_level = next_level

    for node in this_level:

        if node.left or node.right:
            return False

    return True



bst = build_bst(EXAMPLE_LIST)

print(bst.in_order_traversal())
print(check_height(bst))
print(silly_check_balance(bst))
print(smart_check_balance(bst))

bst.insert(1.4)
bst.insert(1.5)
print(bst.in_order_traversal())
print(check_height(bst))
print(silly_check_balance(bst))
print(smart_check_balance(bst))

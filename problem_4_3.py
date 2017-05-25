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


def build_linked_lists_w_none(binary_tree):
    all_linked_lists = []

    current_ll = [binary_tree]

    while current_ll and any(current_ll):

        all_linked_lists.append(current_ll)
        next_ll = []

        for node in current_ll:
            if node is None:
                continue
            if node.left:
                next_ll.append(node.left)
            else:
                next_ll.append(None)
            if node.right:
                next_ll.append(node.right)
            else:
                next_ll.append(None)

        current_ll = next_ll

    return all_linked_lists

def build_linked_lists(binary_tree):
    all_linked_lists = []

    current_ll = [binary_tree]

    while current_ll:

        all_linked_lists.append(current_ll)
        next_ll = []

        for node in current_ll:
            if node.left:
                next_ll.append(node.left)
            if node.right:
                next_ll.append(node.right)

        current_ll = next_ll

    return all_linked_lists

list_of_lists = build_linked_lists(bst)

for l in list_of_lists:
    print([n.value for n in l])

list_of_lists = build_linked_lists_w_none(bst)

def maybe_get_value(node):
    if node:
        return node.value
    else:
        return None

for l in list_of_lists:
    print([maybe_get_value(n) for n in l])

print(bst.right.right.left.value)

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

def interweave(left, right):

    if not left and not right:
        return []

    if not left:
        return [right]

    if not right:
        return [left]

    all_lists = []
    for add_right in interweave(left[1:], right):
        all_lists.append([left[0]] + add_right)

    for add_left in interweave(left, right[1:]):
        all_lists.append([right[0]] + add_left)

    return all_lists

import itertools

def list_possiblilities(bst):

    if bst is None:
        return []

    left_branch = list_possiblilities(bst.left)
    right_branch = list_possiblilities(bst.right)

    if not left_branch and not right_branch:
        return [[bst.value]]

    if not left_branch:
        return [[bst.value] + b for b in right_branch]

    if not right_branch:
        return [[bst.value] + b for b in left_branch]

    all_lists = []

    for l, r in itertools.product(left_branch, right_branch):

        new_lists = [[bst.value] + b for b in interweave(l, r)]

        all_lists.extend(new_lists)

    return all_lists


easy = build_bst(sorted([1, 2, 3, 5, 0, 3.5]))

print(list_possiblilities(easy))



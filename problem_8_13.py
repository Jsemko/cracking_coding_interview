class Box(object):

    def __init__(self, l, w, h):

        self.l = l
        self.w = w
        self.h = h

    def __lt__(self, box):
        return self.l < box.l and self.w < box.w and self.h < box.h

    def __le__(self, box):
        return self.l <= box.l and self.w <= box.w and self.h <= box.h

    def __gt__(self, box):
        return box.__lt__(self)

    def __ge__(self, box):
        return box.__le__(self)

    def __str__(self):
        return 'Box %d, %d, %d' % (self.l, self.w, self.h)

class BoxNode(object):

    def __init__(self, box):
        self.box = box
        self.edges = []
        self.is_root = True
        self.height = None

    def add_edge(self, node):
        self.edges.append(node)
        node.is_root = False


def get_max_each(list_of_boxes):

    if len(list_of_boxes) == 1:
        return [list_of_boxes[0].h]

    new_heights = []

    for i, box in enumerate(list_of_boxes):

        others = list_of_boxes[:i] + list_of_boxes[i+1:]
        other_maxes = get_max_each(others)

        max_addition = 0
        for j, other_box in enumerate(others):
            if box < other_box and  max_addition < other_maxes[j]:
                max_addition = other_maxes[j]

        new_heights.append(max_addition + box.h)

    return new_heights



def get_max_height(list_of_boxes):

    return max(get_max_each(list_of_boxes))

import itertools


def top_sort(list_of_boxes):

    nodes = [BoxNode(box) for box in list_of_boxes]

    for node1, node2 in itertools.combinations(nodes, 2):
        if node1.box < node2.box:
            node1.add_edge(node2)
        elif node1.box > node2.box:
            node2.add_edge(node1)

    def get_height(root):
        height = root.box.h

        if not root.edges:
            return height

        neighbor_heights = []
        for neighbor in root.edges:
            if neighbor.height:
                neighbor_heights.append(neighbor_heights)
            else:
                new_height = get_height(neighbor)
                neighbor.get_height = new_height
                neighbor_heights.append(new_height)

        height += max(neighbor_heights)

        return height

    max_height = 0
    for node in nodes:
        if node.is_root:
            this_height = get_height(node)
            if this_height > max_height:
                max_height = this_height

    return max_height

import random
boxes = []

r = random.randint
m = 1
M = 10

for _ in range(10):

    boxes.append(Box(r(m, M), r(m, M), r(m, M)))
    print(boxes[-1])

print(top_sort(boxes))
print(get_max_height(boxes))



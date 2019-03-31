import itertools

class PersonNode(object):

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.edges = []
        self.max_height_above = None

    def find_my_max_height(self):
        if self.max_height_above:
            return self.max_height_above

        next_heights = [1]
        for next_person in self.edges:
            next_heights.append(next_person.find_my_max_height() + 1)

        self.max_height_above = max(next_heights)
        return self.max_height_above

    def __lt__(self, other):
        return self.weight < other.weight and self.height < other.height

def find_max_height(list_of_tuples):

    nodes = [PersonNode(w, h) for (w, h) in list_of_tuples]

    for n1, n2 in itertools.combinations(nodes, 2):
        if n1 < n2:
            n2.edges.append(n1)
        if n2 < n1:
            n1.edges.append(n2)

    return max(n.find_my_max_height() for n in nodes)


def main():
    tuples = [
        (65, 100),
        (70, 150),
        (56, 90),
        (75, 190),
        (60, 95),
        (68, 110),
    ]

    print(find_max_height(tuples))

if __name__ == '__main__':
    main()

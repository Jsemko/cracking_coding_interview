class Node(object):

    def __init__(self, name):

        self.name = name

        #intially no edges
        self.adjacent = set()

    def add_edge(self, node):

        self.adjacent.add(node)


nodes = [Node(chr(i)) for i in range(97,110)]


for i,j in [(1,2),(4,5),(2,6)]:
    nodes[i].add_edge(nodes[j])

def is_connection(start, stop):

    visited = set()

    queue = [start]

    while queue:

        current = queue[0]
        queue = queue[1:]
        visited.add(current)

        if current == stop:
            return True

        visiting_now = set()
        for node in current.adjacent:
            if node not in visited and node not in visiting_now:
                queue.append(node)
                visiting_now.add(node)

    return False

print(is_connection(nodes[1], nodes[6]))
print(is_connection(nodes[1], nodes[5]))

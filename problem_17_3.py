import random

def gen_rand_selection(m, array):

    assert len(array) >= m, "can't take more than m elements!"

    items = array

    selected = []

    for _ in range(m):
        L = len(items)

        current_card = int(random.random() * L)

        selected.append(items[current_card])

        del items[current_card]

    return selected


print(gen_rand_selection(2, list(range(10))))


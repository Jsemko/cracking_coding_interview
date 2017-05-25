import random

def gen_rand_perm(n):
    items = list(range(n))

    selected = []

    while items:
        L = len(items)

        current_card = int(random.random() * L)

        selected.append(items[current_card])

        del items[current_card]

    return selected


print(gen_rand_perm(52))


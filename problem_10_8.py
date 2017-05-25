#Since I do not have a bit array, I'll just use a boolean

def print_dups(array):
    bit_array = [False] * 32000
    count = 0
    for i in array:
        if bit_array[i]:
            print(i)
            count += 1
        else:
            bit_array[i] = True
    print('total count: %d' % count)
    return

import random

array = [random.randint(0, 32000 - 1) for _ in range(40000)]

print_dups(array)
print(len(array) - len(set(array)))

"""
Find the next largest and next smallest which
have same number of bits in binary rep
"""

def next_largest(N):

    assert int is type(N)
    assert N > 0

    i = 0
    ones_count = 0
    while True:
        if (N >> i) % 2 == 1 and (N >> (i + 1)) % 2 == 0:
            N |= (1 << (i + 1))
            N &= ~((1 << i +1) - 1 )
            N |= ((1 << ones_count) - 1)
            return N
        elif (N >> i) % 2 == 1:
            ones_count += 1
        i += 1

def next_smallest(N):

    assert int is type(N)
    assert N > 0

    i = 0
    ones_count = 0
    while True:
        if (N >> i) % 2 == 0 and (N >> (i + 1)) % 2 == 1:
            N &= ~(1 << (i + 1))
            N |= (1 << i)
            N &= ~((1 << i) - 1)
            N |= ((1 << ones_count) - 1) << (i - ones_count)
            return N
        elif (N >> i) % 2 == 1:
            ones_count += 1
        i += 1
        if (1 << i) > N:
            return None

print(next_largest(5))
print(next_largest(9))
print(next_smallest(5))
print(next_smallest(9))

print(next_smallest(next_largest(9)))

print(bin(13948))
print(bin(next_largest(13948)))

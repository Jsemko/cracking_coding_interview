def flip_to_match(N, M):

    diff = N ^ M
    count = 0
    while diff:
        if diff % 2 == 1:
            count += 1
        diff //= 2

    return count

def flip_to_match2(N, M):

    diff = N ^ M
    count = 0
    while diff:
        count += 1
        diff = (diff & (diff - 1))

    return count

print(flip_to_match(29, 15))
print(flip_to_match2(29, 15))

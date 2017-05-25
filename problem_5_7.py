def flip_even_odd(N):

    mask = (4 ** 16 - 1) // 3

    return ((mask & N) << 1) | ((mask << 1 & N) >> 1)

trial = 0b10001010110

print('-' + str(bin(trial)))
print(bin(flip_even_odd(trial)))

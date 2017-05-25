"""
inputs M, N 32-bit integers, and i < j such that 2 ** (i - j) < M
Goal: fit in N between spots i and j

example N = 10000000000
M = 10011
i = 2
j = 6

gives 10001001100
"""


def insert_M(N, M, i, j):

    shifted_M = M << i
    mask = (2 ** (j - i + 1)) << i
    masked_N = N & ~mask

    return masked_N | shifted_M

M = 0b10011
N = 0b10000000000

i = 2
j = 6

print(bin(insert_M(N, M, i, j)))


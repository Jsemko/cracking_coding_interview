import random

def merge_sorted(A, B, A_length):

    assert len(B) + A_length >= len(A), 'Not enough room!'

    insert_idx = len(A) - 1
    a_idx = A_length - 1
    b_idx = len(B) - 1
    while a_idx >= 0 and b_idx >= 0:
        if A[a_idx] < B[b_idx]:
            A[insert_idx] = B[b_idx]
            b_idx -= 1
        else:
            A[insert_idx] = A[a_idx]
            a_idx -= 1
        insert_idx -= 1
    while a_idx >= 0:
        A[insert_idx] = A[a_idx]
        insert_idx -= 1
        a_idx -= 1
    while b_idx >= 0:
        A[insert_idx] = B[b_idx]
        insert_idx -= 1
        b_idx -= 1


N = 100
M = 50

A = sorted([random.randint(0, 10000) for _ in range(N)])
A.extend([None] * (M))
B = sorted([random.randint(0, 10000) for _ in range(M)])

print('A', A)
print()
print('B', B)
print()
merge_sorted(A, B, N)

print('A', A)

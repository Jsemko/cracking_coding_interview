"""
Explain ((n & (n-1)) == 0)

case 1: n is odd - then n must be 1
case 2: n is even - will borrow so must not be any 1's til the end,
Thus any power of 2 or zeros should work.

"""

def try_it(n):
    return ((n & (n-1)) == 0)

print(try_it(8))

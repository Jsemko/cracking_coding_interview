def prime_list(n):
    l = 1
    primes = [2]
    candidate = 3
    while l < n:
        for p in primes:
            if p ** 2 > candidate:
                primes.append(candidate)
                l += 1
                break
            if candidate % p == 0:
                break
        candidate += 1
    return primes

letter_primes = prime_list(26)

letter_num = lambda n:ord(n) - ord('a')

def key(s):
    prod = 1
    for c in s:
        prod *= letter_num(c)
    return prod

def group_anagrams(str_list):
    return sorted(str_list, key=key)

word_list = ['hi', 'there', 'ih', 'five', 'ivef', 'heret', 'this', 'hist']

word_sorted = group_anagrams(word_list)
print(word_sorted)
print([key(w) for w in word_sorted])

def my_cmp(s1, s2):
    a = sorted(s1)
    b = sorted(s2)
    if a == b:
        return 0
    if a < b:
        return 1
    if a > b:
        return -1

import functools

new_key = functools.cmp_to_key(my_cmp)

alt = sorted(word_list, key=new_key)
print(alt)
value = new_key('a')
print(value)
print([new_key(w) for w in alt])

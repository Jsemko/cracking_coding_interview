

def perm_w_dups(s):

    if len(s) == 0:
        return None

    if len(s) == 1:
        return [s]

    prev = None
    these_perms = []

    for i, element in enumerate(s):
        if element != prev:
            prev = element
            these_perms.extend([[element] + rem for rem in perm_w_dups(s[:i] + s[i+1:])])

    return these_perms



big_perm = lambda l:perm_w_dups(sorted(l))

print(big_perm([1, 2, 3, 3, 3]))
print(len(big_perm([1, 2, 3, 3, 3])))
print(len(big_perm([1] * 6)))

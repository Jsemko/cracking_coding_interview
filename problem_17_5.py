#Find largest subarry w/ equal number of letters and numbers

def running_total(s):
    current = 0
    ends = dict()
    ends[0] = [0, 0]
    for i, c in enumerate(s):
        if c.isalpha():
            current += 1
        else:
            current -= 1
        if current in ends:
            ends[current][1] = i + 1
        else:
            ends[current] = [i + 1, i + 1]
    candidates = ends.values()
    best = -1
    for c in candidates:
        if c[1] - c[0] > best:
            cur = c[:]
            best = c[1] - c[0]
    return s[cur[0]:cur[1]]

print(running_total('abc12aas93eg'))

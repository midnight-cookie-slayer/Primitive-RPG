"""def divisors(l):
    h = [1, l]
    for j in range(l-1, 1, -1):
        if (l % j == 0):
            h.append(j)
    return h

def lsum(k):
    s = 0
    for i in k:
        s = s + i
    return s

def kv(s):
    sqrt = 0
    for i in range(0, 1000000):
        sqrt = s ** (0.5)
    if type(sqrt) == int:
        return sqrt
"""


def make_readable(sec):
    h = 0
    m = 0
    s = 0
    min = m
    if sec // 60 >= 1:
        m += int(sec / 60)
        s += int(sec % 60)
        min += m
    else:
        s += sec
    if min // 60 >= 1:
        h += int(m / 60)
        m = min - h * 60
    return f"{h}:{m}:{s}"


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

n = int(input('введи число: '))
print(make_readable(n))

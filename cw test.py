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


def make_readable(seconds):
    h = 0
    m = 0
    s = 0
    min = m
    if seconds // 60 >= 1:
        m += int(seconds / 60)
        s += int(seconds % 60)
        min += m
    else:
        s += seconds
    if min // 60 >= 1:
        h += int(m / 60)
        m = min - h * 60
    sec = str(s)
    min = str(m)
    hour = str(h)
    if len(sec) < 2:
        sec = '0' + sec
    if len(min) < 2:
        min = '0' + min
    if len(hour) < 2:
        hour = '0' + hour
    return f"{hour}:{min}:{sec}"


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

n = int(input('введи число: '))
print(make_readable(n))

import sys
input = sys.stdin.readline
M = int(input())
s = set()

for _ in range(M):
    cal, *rest = input().split()
    x = int(rest[0]) if rest else None

    if cal == 'add':
        s.add(x)
    if cal == 'remove':
        s.discard(x)
    if cal == 'check':
        print(1 if x in s else 0)
    if cal == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)
    if cal == 'all':
        s = set(range(1,21))
    if cal == 'empty':
        s.clear()
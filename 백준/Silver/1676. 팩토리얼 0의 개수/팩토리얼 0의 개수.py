import math
N = int(input())

total = math.factorial(N)

ch = str(total)[::-1]

cnt = 0
for c in ch:
    if c == '0':
        cnt += 1
    else:
        break
print(cnt)
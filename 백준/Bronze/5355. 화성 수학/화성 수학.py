case = int(input())

for _ in range(case):
    n = list(map(str,input().split()))
    result = float(n[0])
    for i in range(len(n)):
        if n[i] == '@':
            result *=3
        elif n[i] == '%':
            result += 5
        elif n[i] == '#':
            result -=7
    print(f'{result:.2f}')
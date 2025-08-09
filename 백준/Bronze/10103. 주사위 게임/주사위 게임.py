cy = sd = 100

n = int(input())

for i in range(n):
    a,b = map(int,input().split())

    if a>b:
        sd -= a
    elif a<b:
        cy -= b
    
print(f'{cy}\n{sd}')
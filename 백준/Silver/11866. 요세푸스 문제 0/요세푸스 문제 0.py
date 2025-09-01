N, K = map(int,input().split())
people = list(range(1,N+1))
del_list = []
index = 0

while people:
    index = (index + K-1) % len(people)
    del_list.append(people.pop(index))

print('<',end='')
for d in range(N-1):
    print(del_list[d],end=', ')
print(del_list[N-1],end='')
print('>',end='')
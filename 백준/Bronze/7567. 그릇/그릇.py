n = input()
count = 10
for i in range(1,len(n)):
    if n[i-1] == n[i]:
        count+=5
    else:
        count+=10
print(count)
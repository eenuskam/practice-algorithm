N = int(input())
size = list(map(int,input().split())) 
T,P = map(int,input().split()) 

count_t = 0

for s in size:
    if s == 0:
        continue
    elif s < T:
        count_t+=1
    elif s % T == 0 :
        count_t+= s//T
    elif s > T:
        count_t+= s//T+1

print(count_t)
print(N//P, N%P)   
N,K = map(int,input().split())

a = 1
b = 1

# arr_n = list(range(1,N+1))
arr_n = [n for n in range(1,N+1)]
arr_n.sort(reverse=True)

for k in range(K):
    a *= arr_n[k]
    b *= (k+1)
    
print(int(a/b))

T = int(input())

for i in range(T):
    K = int(input()) 
    N = int(input()) 
    k0 = [x for x in range(1,N+1)] 
    for k in range(K): 
        for n in range(1,N): 
            k0[n] += k0[n-1] 
    print(k0[-1])
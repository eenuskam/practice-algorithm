while True:
    n = int(input())
    if n==-1:
        break
    
    total = []
    for i in range(1,n):
        if n % i == 0:
            total.append(i)  
    if sum(total) == n:
        print(n,'=',' + '.join(str(i) for i in total))
    else:
        print(f'{n} is NOT perfect.')
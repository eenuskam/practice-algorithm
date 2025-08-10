T = int(input())

for t in range(T):
    N = int(input())
    school = ''
    drunk = 0
    
    for i in range(N):
        s,d = input().split()
        d = int(d)
        
        if drunk < d:
            drunk = d
            school = s
    print(school)
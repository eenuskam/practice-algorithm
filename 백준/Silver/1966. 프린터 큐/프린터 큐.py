from collections import deque

T = int(input())

for _ in range(T): 
    N,M = map(int,input().split())
    score = list(map(int,input().split()))
    
    result = 1
    while score:
        if score[0] < max(score):
            score.append(score.pop(0))
        else:
            if M == 0: break

            score.pop(0)
            result += 1
        M = M-1 if M > 0 else len(score) - 1
    print(result)
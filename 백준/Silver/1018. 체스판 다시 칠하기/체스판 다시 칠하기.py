import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

result = []

for i in range(N - 7):          
    for j in range(M - 7):      
        draw1 = 0  
        draw2 = 0  

        
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                cur = board[a][b]               
                if (a + b) % 2 == 0:                  
                    if cur != 'B':  
                        draw1 += 1
                    if cur != 'W':  
                        draw2 += 1
                else:    
                    if cur != 'W':  
                        draw1 += 1
                    if cur != 'B':  
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))
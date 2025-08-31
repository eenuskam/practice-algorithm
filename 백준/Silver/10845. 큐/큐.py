import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
stack = deque()

for _ in range(N):
    word, *num = input().split() 
    num = int(num[0]) if num else None 

    if word == 'push':
        stack.append(num)
    elif word == 'pop':
        if stack:
            del_num = stack.popleft()
            print(del_num)
        else:
            print(-1)
    elif word == 'size':
        print(len(stack))
    elif word == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif word == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif word == 'back':
        if stack:
            print(stack[-1])
        else:   
            print(-1)
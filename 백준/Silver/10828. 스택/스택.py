from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack  = deque()

for _ in range(N):
    word, *num = input().split()
    num = int(num[0]) if num else None
    
    if word == 'push':
        stack.append(num)
    elif word == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            del_num = stack.pop()
            print(del_num)
    elif word == 'size':
        print(len(stack))
    elif word == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif word == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
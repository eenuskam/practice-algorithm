T = int(input())
for _ in range(T):
    string = input()
    stack = []

    for ch in string:
        if ch == '(' :
            stack.append(ch)
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
                break
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
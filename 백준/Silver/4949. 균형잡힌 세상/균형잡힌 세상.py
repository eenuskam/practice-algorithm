while True:
    string = input()
    stack = []
    
    if string == '.':
        break

    for ch in string:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == ']':
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else:
                stack.append(']')
                break
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
              stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
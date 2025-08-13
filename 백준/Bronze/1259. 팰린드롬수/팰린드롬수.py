while True:
    num = int(input())
    if num == 0:
        break
    if list(reversed(str(num))) == list(str(num)):
        print('yes')
    else:
        print('no')
while True:
    num = input()
    if int(num) == 0:
        break
    if list(reversed(num)) == list(num):
        print('yes')
    else:
        print('no')
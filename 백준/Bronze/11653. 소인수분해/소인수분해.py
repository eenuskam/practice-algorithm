a = int(input())
for i in range(2,a+1) :
    while True :
        if a%i == 0 :
            a = a // i
            print(i)
        else :
            break
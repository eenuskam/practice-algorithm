n = int(input())
i = 0
cnt = 0
while True:
    if n > i : #s가 i보다 크면 s에서 i를 차감
        i += 1
        n -= i
        cnt += 1
    else:
        print(cnt)
        break 
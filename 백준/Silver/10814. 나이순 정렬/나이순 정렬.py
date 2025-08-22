import sys
input = sys.stdin.readline
N = int(input())

datas = [input().split() for _ in range(N)]

datas.sort(key=lambda x: int(x[0]))

for data in datas:
    print(data[0],data[1])
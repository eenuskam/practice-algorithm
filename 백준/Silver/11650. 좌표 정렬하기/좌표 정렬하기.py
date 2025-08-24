N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]

nums.sort()
for n in nums:
    print(n[0],n[1])
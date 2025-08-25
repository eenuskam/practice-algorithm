N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]

nums.sort(key = lambda num : (num[1],num[0]))
for n in nums:
    print(n[0],n[1])
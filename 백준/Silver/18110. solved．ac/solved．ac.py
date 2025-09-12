import sys
input = sys.stdin.readline

n = int(input())

def roundup(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if n == 0:
    print(0)
else:
    nums = [int(input()) for _ in range(n)]
    
    nums.sort()
    border = roundup(n*0.15)
    new_nums = nums[border:n-border]
    print(roundup(sum(new_nums)/len(new_nums)))
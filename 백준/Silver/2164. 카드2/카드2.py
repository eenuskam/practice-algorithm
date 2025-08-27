from collections import deque

N = int(input())
nums = deque(range(1,N+1))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())
print(nums[0])
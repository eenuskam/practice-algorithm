import statistics

N = int(input())
score = list(map(int,input().split()))
M = max(score)
new_score = [s/M*100 for s in score]
print(statistics.mean(new_score))
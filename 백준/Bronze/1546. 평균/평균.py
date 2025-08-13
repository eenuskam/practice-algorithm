import statistics
N = int(input())
score = list(map(int,input().split()))
M = max(score)
score_list = []

for s in score:
    new_score = s/M*100
    score_list.append(new_score)
print(statistics.mean(score_list))
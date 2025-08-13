L = int(input())
word = list(str(input()))
score = 0

for i,w in enumerate(word):
    hash = (ord(w)-96)*(31**i)
    score +=hash
print(score)
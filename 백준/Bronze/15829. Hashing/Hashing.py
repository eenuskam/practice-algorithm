r = 31; M = 1234567891

L = int(input())
word = list(str(input()))
score = 0

for i,w in enumerate(word):
    hash = (ord(w)-96)*(r**i)
    score +=hash
print(score%M)
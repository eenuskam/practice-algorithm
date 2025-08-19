N = int(input())
words = [input() for _ in range(N)]

words = list(set(words))

words.sort(key = lambda x : (len(x),x))
for w in words:
    print(w)
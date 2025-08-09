N = int(input())
vote = []

for n in range(N):
    v = int(input())
    vote.append(v)

vote_0 = vote.count(0)
vote_1 = vote.count(1)

if vote_0 > vote_1:
    print('Junhee is not cute!')
elif vote_0 < vote_1:
    print('Junhee is cute!')
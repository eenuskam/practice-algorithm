N = int(input())
vote = input()

vote_A = vote.count('A')
vote_B = vote.count('B')

if vote_A > vote_B:
    print('A')
elif vote_A < vote_B:
    print('B')
elif vote_A == vote_B:
    print('Tie')
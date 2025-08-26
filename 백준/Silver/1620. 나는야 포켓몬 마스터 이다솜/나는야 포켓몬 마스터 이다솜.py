import sys
input = sys.stdin.readline

N, M = map(int,input().split())

by_id = {}
by_name = {}

for n in range(N):
    pokemon = input().rstrip()
    by_id[n] = pokemon
    by_name[pokemon] = n

for _ in range(M):
    quiz = input().rstrip()
    if quiz.isdigit() == True :
        print(by_id[int(quiz)-1])
    else:
        print(by_name[quiz]+1)
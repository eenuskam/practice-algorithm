N = int(input())
card_list = list(map(int,input().split()))
M = int(input())
have_list = list(map(int,input().split()))

card_dic = {}
for card in card_list:
    if card in card_dic:
        card_dic[card] +=1
    else:
        card_dic[card] = 1

for card in have_list:
    if card in card_dic:
        print(card_dic[card],end=' ')
    else:
        print(0,end=' ')
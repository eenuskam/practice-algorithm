h,m,s = map(int,input().split())
t = int(input()) # 6015

s +=t
m+=s//60
h+=m//60
print(h%24,m%60,s%60)
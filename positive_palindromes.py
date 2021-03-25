# All integers positive & any palindromic integer present?
# HackerRank any or all

n, integers =input(), input().split()

print(all(map(lambda n:int(n)>-1,integers)) and any(map(lambda x:x==x[::-1],integers)) )

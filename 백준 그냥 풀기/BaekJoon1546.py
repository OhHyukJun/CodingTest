import sys
n = input()
num = list(map(int, input().split()))
nummax = max(num)
total = sum(num)
print(total/nummax*100/int(n))

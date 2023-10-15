n = int(input())
a = n//4
ans = 'int'

for i in range(a):
    ans = 'long ' + ans
print(ans)
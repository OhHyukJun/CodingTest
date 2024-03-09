'''
괄호 문자열은 '(',')' 만으로 구성되어있다
올바른 괄호 문자열(VPS)
한 쌍의 괄호 기호로 된 "()" 문자열은 기본 VPS
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 
그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

'''
T = int(input())
arr = []
for i in range(T):
    str = input()
    arr.append(str)

for i in range(len(arr)):
    count = 0
    for j in range(len(arr[i])):
        if arr[i][j] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')
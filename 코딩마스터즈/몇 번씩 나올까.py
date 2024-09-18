import sys 

n = int(input())
arr = []
answer = []
for i in range(n):
    temp = list(str(i+1))
    arr.append(temp)
answer = [0]*10

for i in arr:
    answer[0] += i.count('0')
    answer[1] += i.count('1')
    answer[2] += i.count('2')
    answer[3] += i.count('3')
    answer[4] += i.count('4')
    answer[5] += i.count('5')
    answer[6] += i.count('6')
    answer[7] += i.count('7')
    answer[8] += i.count('8')
    answer[9] += i.count('9')

for i in answer:
    if i == 9:
        print(i)
    print(i,end=" ")
    
#1부터 n까지의 수를 스택에 저장하고 출력하는 방시긍로 하나의 수열을 만들 수 있다
#이 때 스택에 push하는 순서는 반드시 오흠차순을 지키도록 가정
#이러한 방식으로 스택을 이용해 주어진 수열을 만들 수 있는지 확인하고 만들 수 있다면 
#어떤 순서로 push와 pop을 수행햐애 하는지 확인하느 프로그램
#입력: 1번째 줄에는 n 2번째 줄에서 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 1개씩
#출력: 수열을 만들기 위한 연산 순서를 출력 push연산은 + , pop 연산은 -로 출력 

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1 #오름차순 자연수
result = True
ans = ""

for i in range(N):
    s = A[i]
    if s >= num: #현재 수열값이 오름차순 자연수보다 크거나 같다면 append실행
        while s >=num:
            stack.append(num)
            num += 1
            ans += "+\n" #+를 출력함
        stack.pop()
        ans += "-\n" #-를 출력함
    else: #현재 수열값이 오름차순 자연수보다 작다면 pop실행
        n = stack.pop()
        if n>s:
            print("NO")
            result = False
            break #while문을 break함
        else:
            ans += "-\n"

if result:
    print(ans)
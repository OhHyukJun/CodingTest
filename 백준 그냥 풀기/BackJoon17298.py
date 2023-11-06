#수열 A의 크기는 N -> 오큰수 NGE(i)를 구하자
#오큰수가 없다면? -> -1 출력
#1.N, A를 설정하고 NGE설정
N = int(input())
A = list(map(int,input().split()))
ans = [0]*N
myStack = [] #스택 선언

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]: 
        #스택이 비어있지 않고 현재 스택이 스택 top 인덱스가 가르키는 수열보다 큰 경우
        ans[myStack.pop()] = A[i] #오큰수를 현재 수열로 저장
    myStack.append(i) #스택에는 값이 아닌 값의 인덱스를 저장한다
    
while myStack: #스택이 비어있을 때까지 반복
    ans[myStack.pop()] = -1 #스택에 쌓인 인덱스에 -1을 출력
    
result=""
     
for i in range(N):
    result+=str(ans[i])+" "#공백을 넣어서 출력

print(result)
#left right 위주로 풀기!
def solution(n, left, right):
    answer = []
    arr = []
    for i in range(left,right+1):
        if i < n:
            answer.append(i+1)
        elif i%n <= i//n:
            answer.append(i//n+1)
        else:
            answer.append(i%n+1)
            #print(i%n,i//n)
            #print(i//n+1)
        
    return answer


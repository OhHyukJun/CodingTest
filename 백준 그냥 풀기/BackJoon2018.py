n = int(input())
count = 1 #입력값만 들어간 경우를 포함한 초기화
sum = 1
start_index=1
end_index=1

while end_index !=n:
    if sum==n:
        count+=1
        end_index+=1
        sum+=end_index
    elif sum>n:
        sum-=start_index
        #연속된 자연수에서 왼쪽값을 삭제
        start_index+=1
    else:
        end_index+=1
        #연속된 자연수에서 오른쪽으로 이동
        sum+=end_index

print(count)
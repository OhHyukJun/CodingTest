T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    arr = []
    for _ in range(num):
        arr.append(list(map(int,input().rstrip())))
    answer=0
    for i in range(num//2,-1,-1):
        for j in range(num//2-i,num-(num//2-i)):
            answer += arr[i][j]
            if i != num // 2:
                answer += arr[num-i-1][j]
        
    print(f"#{test_case} {answer}")
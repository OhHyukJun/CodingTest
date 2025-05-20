T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    answer = [0] * num
    
    i = 0
    j = 0
    turn = 0
    while True:
        if turn % 2 == 0:
            while answer[arr[i]-1] != 0:
                i += 1
            answer[arr[i]-1] = "A"
            i += 1
        else:
            while answer[arr1[j]-1] != 0:
                j += 1
            answer[arr1[j]-1] = "B"
            j += 1
        turn += 1
        if turn == num:
            break
    for i in range(num):
        print(answer[i], end="")
    print("")
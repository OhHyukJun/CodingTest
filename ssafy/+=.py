T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    x, y, n = list(map(int,input().split()))
    while x <= n and y <= n:
        if x < y:
            x += y
        else:
            y += x
        answer += 1
    print(answer)
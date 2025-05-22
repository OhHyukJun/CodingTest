T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str = list(input())
    for i in range(10):
        if i == 0:
            continue
        elif  str[0:i] == str[i:i+i]:
            print(f"#{test_case} {i}")
            break
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # P, Q, R, S, W
    # 1리터 당 p
    # 기본 요금은 Q R 이상이면 1리터 당 S
    # 수도 사용 양 W 
    p,q,r,s,w = map(int,input().split())
    if w > r:
        if p * w > q + (w-r) * s:
            print(f"#{test_case} {q + (w-r) * s}")
        else:
            print(f"#{test_case} {p*w}")
    else:
        if p * w > q:
            print(f"#{test_case} {q}")
        else:
            print(f"#{test_case} {p*w}")
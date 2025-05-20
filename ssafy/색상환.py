T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
colors = ["red","orange","yellow","green","blue","purple"]
for test_case in range(1, T + 1):
    # 빨강색(red), 오렌지색(orange), 노란색(yellow), 초록색(green), 파랑색(blue), 보라색(purple)
    a,b = input().strip().split()
    if a == b:
        print("E")
    elif (colors.index(a) -1) == colors.index(b) or (colors.index(a) +1) == colors.index(b):
        print("A")
    elif (colors.index(a) == 0 and colors.index(b) == 5) or (colors.index(a) == 5 and colors.index(b) == 0):
        print("A")
    elif (colors.index(a) - colors.index(b) == 3) or colors.index(a) - colors.index(b) == -3:
        print("C")
    else:
        print("X")
    # print(colors.index(a),colors.index(b))
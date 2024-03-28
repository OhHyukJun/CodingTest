def solution(numbers):
    # 초기 답 배열을 -1로 설정합니다.
    answer = [-1] * len(numbers)
    # 인덱스를 저장할 스택을 초기화합니다.
    stack = []

    for i, number in enumerate(numbers):
        # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 인덱스에 해당하는 숫자보다 클 때까지 반복합니다.
        while stack and number > numbers[stack[-1]]:
            answer[stack.pop()] = number
        # 현재 숫자의 인덱스를 스택에 추가합니다.
        stack.append(i)

    return answer

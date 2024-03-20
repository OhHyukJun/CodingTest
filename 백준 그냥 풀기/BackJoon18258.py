'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
answer = deque()

for _ in range(N):
    arr = input().split()
    if arr[0] == 'push':
        answer.append(arr[1])
    elif arr[0] == 'pop' and answer:
        print(answer.popleft())
    elif arr[0] == 'size':
        print(len(answer))
    elif arr[0] == 'empty' and answer:
        print(0)
    elif arr[0] == 'back' and answer:
        print(answer[-1])
    elif arr[0] == 'front' and answer:
        print(answer[0])
    elif len(answer) == 0:
        if arr[0] == 'empty':
            print(1)
        else:
            print(-1)
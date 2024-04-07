'''
알파넷 소문자로 이루어진 문자열을 가지고 시작
같은 알파벳 2개 붙어있는 짝을 찾는다
반복해서 문자열을 모두 제거한다면 짝지어 제거하기 종료
'''
from collections import deque

def solution(s):
    #answer = -1
    q = deque(s)
    arr = []
    while q:
        a = q.popleft()
        if len(arr) != 0 and a == arr[-1]:
            arr.pop()
        else:
            arr.append(a)
        
            
    if len(arr) == 0:
        return 1
    else:
        return 0

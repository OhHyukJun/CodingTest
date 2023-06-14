import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

def special(num):
    for i in range(2, int(num/2+1)):
        if num % i==0:
            return False
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0: #짝수라면 더는 탐색하지 않음
                continue
            if special(number * 10 + i): # 소수이면 증가
                DFS(number * 10 + i)
                
DFS(2)
DFS(3)
DFS(5)
DFS(7)
#일의 자리 소수는 2,3,5,7이므로 4가지 수 에서만 시작
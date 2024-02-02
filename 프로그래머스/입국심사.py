'''
- n명
- 모든 사람이 심사를 받는데 걸리는 최소 시간
- 가장 앞 사람이 비어있는 심삳에서 심사를 받을 수 있지만 더 빨리 끝나는 심사대가 있으면 거기서 심사
- 1 <= n <= 1,000,000,000 / 1 <= time <= 1,000,000,000 / 1 <= 심사관 <= 1,000,000
'''

n = 6
times = [7,10]

def solution(n,times):
    times = sorted(times)
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start+end) // 2
        total = 0
        for time in times:
            total += mid // time
            if total >= n:
                break
        if total >= n:
            end = mid - 1
        else:
            start = mid + 1
    print(start)

solution(n,times)
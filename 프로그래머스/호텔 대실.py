def solution(book_time):
    answer = [0] * 1440
    
    for times in book_time:
        start_h,start_m = map(int, times[0].split(':'))
        end_h, end_m = map(int,times[1].split(':'))
        start = start_h * 60 + start_m
        end = end_h * 60 + end_m + 10
        
        if end > 1440: end = 1440 #24시가 넘지 않도록 설정
        
        for i in range(start,end):
            answer[i] += 1 #전체 경우의 수를 계산
            
    return max(answer)
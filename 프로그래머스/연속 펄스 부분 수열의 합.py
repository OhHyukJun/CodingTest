from sys import maxsize
def solution(sequence):
    answer = -maxsize  
		# answer는 최대 합을 저장할 변수. 초기값으로는 가능한 최소값을 설정합니다.
    sum = sum1 = 0  
		# sum과 sum1은 각각 1, -1로 시작하는 펄스 수열을 적용했을 때의 합을 저장
    n = len(sequence)  
    min_sum = min_sum1 = 0  
		# min_sum과 min_sum1은 각각 sum과 sum1의 최소값을 저장합니다.
    for i in range(n):  
        if i % 2 == 0:  
            sum += sequence[i] 
            sum1 -= sequence[i]  
        else:
            sum -= sequence[i] 
            sum1 += sequence[i]  
        
        answer = max(answer,sum-min_sum,sum1-min_sum1)  
				# 현재까지의 최대 합을 계산합니다.
        
        min_sum = min(min_sum,sum)  # sum의 최소값을 업데이트합니다.
        min_sum1 = min(min_sum1,sum1)  # sum1의 최소값을 업데이트합니다.
        
    return answer  # 최대 합을 반환합니다.
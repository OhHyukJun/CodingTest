'''
x의 모든 0 을 제거
len(x) = c 일 떄, c를 이진법으로 표현한 문자열로 변환
x="0111010" 일 때, 변환 횟수와  1일 될 때까지 변환해서 사라진 0의 갯수를 출력
'''
def solution(s):
    a,count = 0,0
    while s != "1":
        count_one = s.count("1")
        count += len(s) - count_one
        s = format(count_one,'b')
        a+=1
        
    
    return a,count
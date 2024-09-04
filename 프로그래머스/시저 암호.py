def solution(s, n):
    answer = ''
    s = list(s)

    for i in s:#65 90 #97 122
        if 65 <= ord(i) <= 90 and  ord(i) + n <= 90:
            answer += chr(ord(i)+n)
        elif 65 <= ord(i) <= 90 and  ord(i) + n > 90:
            answer += chr(65+ord(i)+n-90-1)
        elif 97 <= ord(i) <= 122 and  ord(i) + n <= 122:
            answer += chr(ord(i)+n)
        elif 97 <= ord(i) <= 122 and  ord(i) + n > 122:
            answer += chr(97+ord(i)+n-122-1)    
        elif i == " ":
            answer += " "
        
    return answer
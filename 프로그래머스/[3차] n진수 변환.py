def solution(n, t, m, p):
    answer = ''
    text = '0'
    n_len = t*m
    n_dict = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
    for i in range(n_len):
        num=''
        while i:
            num += n_dict[i%n]
            i //=n
        text+=num[::-1]
    
    text = list(text)[:n_len]

    for i in range(p-1,n_len,m):
        answer += text[i]
    return answer
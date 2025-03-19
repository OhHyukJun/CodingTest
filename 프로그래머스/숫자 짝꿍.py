from collections import Counter

def solution(X, Y):
    answer = []
    X_count = Counter(X)
    Y_count = Counter(Y)
    X = list(X)
    Y = list(Y)

    for num in X_count.keys():
        if num in Y_count:
            answer.append(num*min(X_count[num],Y_count[num]))
    if not answer:
        return '-1'
    else: 
        answer.sort(reverse=True)
        answer = ''.join(answer)
    if answer.count('0') == len(answer):
        return '0'
    return answer
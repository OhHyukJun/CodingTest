
def solution(elements):
    answer = set()
    n = len(elements)
    elements = 2 * elements
    #list = []
    for i in range(n):
        for j in range(n):
            answer.add(sum(elements[i:i+j+1]))
    
    return len(answer)
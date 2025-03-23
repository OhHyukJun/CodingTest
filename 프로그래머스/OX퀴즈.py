def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quiz[i] = quiz[i].split()
    for i in range(len(quiz)):
        temp = 0
        for j in range(len(quiz[i])):
            if quiz[i][j] == '-':
                temp = int(quiz[i][j-1]) - int(quiz[i][j+1])
                if str(temp) == quiz[i][j+3]:
                    answer.append('O')
                else:
                    answer.append('X')
            if quiz[i][j] == '+':
                temp = int(quiz[i][j-1]) + int(quiz[i][j+1])
                if str(temp) == quiz[i][j+3]:
                    answer.append('O')
                else:
                    answer.append('X')
    return answer
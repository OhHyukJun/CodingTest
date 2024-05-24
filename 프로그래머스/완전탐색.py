def solution(answers):
    answer = []
    arr = [1,2,3,4,5]
    arr1 = [2,1,2,3,2,4,2,5]
    arr2 = [3,3,1,1,2,2,4,4,5,5]
    arr3 = []
    #print(answers)
    #print(answers)
    one,two,three = 0,0,0
    for i in range(len(answers)):
        if answers[i] == arr[i%len(arr)]:    
            one+=1
        if answers[i] == arr1[i%len(arr1)]:
            two+=1
        if answers[i] == arr2[i%len(arr2)]:
            three+=1
    if one == two and two == three:
        return [1,2,3]
    elif one == two and two > three:
        return [1,2]
    elif one == three and three > two:
        return [1,3]
    elif two == three and two > one:
        return [2,3]
    elif one > two and one > three:
        return [1]
    elif two > one and two > three:
        return [2]
    elif three > two and three > one:
        return [3]
    #return answer
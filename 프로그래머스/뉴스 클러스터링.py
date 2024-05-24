def change(text):
    text = list(text.lower())
    text_list = []
    for i in range(len(text)-1):
        temp1 = ord(text[i])
        temp2 = ord(text[i+1])
        if (temp1 <= 122 and temp1 >= 97) and (temp2 <= 122 and temp2 >= 97):
            text_list.append(text[i]+text[i+1])
    text_list.sort()
    return text_list

def solution(str1, str2):
    answer = 0
    str1 = change(str1)
    str2 = change(str2)
    
    intersection = []
    union = str1+str2
    
    if str1 == [] and str2 == []:
        return 65536
    
    for i in range(len(str1)):
        if str1[i] in str2:
            intersection.append(str1[i])
            str2.remove(str1[i])
            
    for i in intersection:
        if i in union:
            union.remove(i)
            
    answer = len(intersection) / len(union)
    
    return int(answer * 65536)
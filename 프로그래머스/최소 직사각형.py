def solution(sizes):
    max_width = 0
    max_height = 0
    
    for w,h in sizes:
        if w < h:
            w,h = h,w
        if w > max_width:
            max_width = w
        if h > max_height:
            max_height = h
    answer = max_width * max_height
    #print(sizes)
    return answer
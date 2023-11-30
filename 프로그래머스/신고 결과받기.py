def solution(id_list, report, k):
    answer = []
    report_dict = dict.fromkeys(id_list,0)
    report_count = dict.fromkeys(id_list,[])
    
    for i in report:
        key, value = i.split()
        report_count[value] = report_count[value] + [key]
        
    for i in report_count.values():
        i = list(set(i))
        if len(i) >= k:
            for j in i:
                report_dict[j] += 1
                
    answer = list(report_dict.values())        
    return answer
import itertools

N = str(input())
N_list = list(N)
arr = [[] for _ in range(len(N_list))]
if len(N_list) > 2:
    for i in range(1,len(N_list)):
        arr[i-1] = list(itertools.combinations(N_list,i))
else:
    arr[0] = list(itertools.combinations(N_list,1))
    
answer = 0

for i in arr:
    for j in i:
        if int(N) % int("".join(j)) == 0:
            answer = 1
            break

if answer == 0:
    print('NO')
else:
    print('YES')
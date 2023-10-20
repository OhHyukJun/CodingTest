dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

line = input()

result = 0

for i in range(len(line)):
    for j in dial:
        if line[i] in j:
            result += dial.index(j) + 3

print(result)


import string

str = [["" for j in range(50)] for i in range(25)]
forLoopParam = [""] * 90
rightHandParam = [["" for j in range(40)] for i in range(10)]
leftHandParam = [""] * 90

j = k = i = m = n = q = s = 0
flag = [0] * 10
count = [0] * 10

print("\nInput the loop to be optimized:")
str[0] = input()

# PROCESSING FIRST LINE FOR DECLARATION
i = str[0].find(";") + 1
i = str[0].find(";", i) + 1
while str[0][i] != ')':
    if str[0][i].isalpha():
        forLoopParam[j] = str[0][i]
        j += 1
    i += 1
i = 0

# PROCESSING SECOND LINE...{
# print(str[0])
str[0] = input()
while str[0][i] != '{':
    # print(str[0][i], end='')
    i += 1
# print()

k = 0
while True:
    str[k] = input()
    if str[k][0] == '}':
        break
    i = str[k].find('=') + 1
    leftHandParam[n] = str[k][i-2]
    n += 1
    k += 1
    i = 0

# N IS THE INDEX TO TEMPCHANGE ARRYA
# TEMPCHANGEARRAY STORES LEFT SIDE PARAMETERS OF ASSIGNMENTS
# OPERATIONS
for m in range(k):
    i = str[m].find('=') + 1
    while str[m][i] != ';':
        if str[m][i].isalpha():
            rightHandParam[m][count[m]] = str[m][i]
            count[m] += 1
        i += 1
    i = 0

# Q IS THE INDEX TO TEMP2
# COMPARING LEFT HAND PARAMETERS WITH RIGHT HAND PARAMETERS
for m in range(k):
    for s in range(count[m]):
        for i in range(n):
            if rightHandParam[m][s] == leftHandParam[i]:
                flag[m] = 1

# COMPARING LEFT HAND SUDE PARAMETERS WITH FOR LOOP
# PARAMETERS
print("Optimized code:")
for i in range(k):
    for q in range(j):
        if leftHandParam[i] == forLoopParam[q]:
            flag[i] = 1

# COMPARING RIGHT HAND PARAMETERS WITH FOR LOOP PARAMETERS
for m in range(k):
    for s in range(count[m]):
        for i in range(j):
            if rightHandParam[m][s] == forLoopParam[i]:
                flag[m] = 1

# DISPLAYING STATEMENTS OF FOR LOOP WHICH CAN BE OPTIMIZED IN THE FOR LOOP
for i in range(k):
    if flag[i] == 1:
        print(str[i])

# DISPLAYING STATEMENTS OF FOR LOOP WHICH CAN BE OPTIMIZED OUTSIDE FOR LOOP
print(str[k], end='\n')
for i in range(k):
    if flag[i] == 0:
        print(str[i], end='')

print()

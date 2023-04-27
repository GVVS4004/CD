ip = ""
op = []
arg1 = []
arg2 = []
res = []
r = ['1', '2', '3', '4', '5']
l = 0
p = 0
j = 0

def rep(a, b, c):
    global j, ip, op, arg1, arg2, r, l
    op.append(ip[b])
    arg1.append(ip[a])
    arg2.append(ip[c])
    ip = ip[:a] + r[j] + ip[b+1:]
    l -= 2
    j += 1

def check(i, c):
    global j, ip, op, arg1, r, l
    if c == '-':
        if not ip[i-1].isalpha():
            op.append('m')
            arg1.append(ip[i+1])
            ip = ip[:i] + r[j] + ip[i+2:]
            l -= 1
            j += 1

def oppr(c):
    if c == '*' or c == '/':
        return 6
    elif c == '+' or c == '-':
        return 5
    elif c == '=':
        return 4

ip = input("Enter the input Expression: ")
l = len(ip)
print(l)
for i in range(l):
    print(ip[i])
    p = oppr(ip[i])
    if p == 5:
        check(i, ip[i])

for i in range(l):
    p = oppr(ip[i])
    if p == 6:
        rep(i-1, i, i+1)
        i = 0

for i in range(l):
    p = oppr(ip[i])
    if p == 5:
        rep(i-1, i, i+1)
        i = 0

for i in range(l):
    p = oppr(ip[i])
    if p == 4:
        rep(i-1, i, i+1)
        i = 0

print("The triple notation is:")
print("op\targ1\targ2")
for i in range(j):
    print(op[i], "\t", arg1[i], "\t", arg2[i])

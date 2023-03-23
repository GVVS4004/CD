character_stream=input("Enter the character stream : ")
x=character_stream.split(" ")
tokens=[]
op=["=","+","-","*","/","**","%"]
num=["0","1","2","3","4","5","6","7","8","9","."]
p=[]
j=1
c=0
f=0
for i in range(len(x)):
    if x[i] in op:
        c=1
        tokens.append("<"+x[i]+">")
        p.append("This is an"+" "+x[i]+" "+"operator")
    if c==0:
        q=x[i]
        for k in range(len(q)):
            if q[k] in num:
                f+=1
        if f==len(q):
            tokens.append(q)
            p.append("This is a numeric value")
        else:
            tokens.append("<"+"id"+str(j)+">")
            p.append("This is an identifier")
            j+=1
        f=0
    c=0
print("LEXEME\t\tTOKEN\t\tPATTERN")
for i in range(len(x)):
    print(x[i],end="\t\t")
    print(tokens[i],end="\t\t")
    print(p[i])

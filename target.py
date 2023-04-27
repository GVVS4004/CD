# with open("exe.txt", "r") as f1, open("exe1.txt", "w") as f2:
#     s = []
#     len = 0
#     for line in f1:
#         words = line.split()
#         if len == 30:
#             break
#         s.append(words[0])
#         len += 1

#     for i in range(len):
#         if s[i] == "=":
#             f2.write("\nLDA\t" + s[i+1])
#             if s[i+2] == "+":
#                 f2.write("\nADD\t" + s[i+3])
#             if s[i+2] == "-":
#                 f2.write("\nSUB\t" + s[i+3])
#             f2.write("\nSTA\t" + s[i-1])


expr = {"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}

with open("IntermediateCode.txt", "r") as file:
    for i in file.readlines():
        flag = False
        s = i[:len(i)-1]
        t = s.split("=")
        prev = ""
        for char in t[1]:
            prev = prev.strip()
            if expr.get(char, -1)!=-1:
                print(f"LDA {prev}")
                print(f"{expr[char]}", end=" ")
                flag = True
                prev = ""
            else:
                prev += char
        if prev:
            if flag:
                print(prev)
            else:
                print(f"LDA {prev}")
        print(f"STA {t[0]}")
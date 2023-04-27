# Symbol Table

import random

expr = "a + b * c"
operators = "+*/^%"

identifier = ""
for i in range(len(expr)):
    if expr[i] in operators:
        print(identifier, random.randint(10**8, 10**9), "Identifier", sep="\t\t")
        print(expr[i].strip(), random.randint(10**8, 10**9), "Operator", sep="\t\t")
        identifier = ""
    else:
        identifier += expr[i].strip()
if identifier:
    print(identifier, random.randint(10**8, 10**9), "Identifier", sep="\t\t")
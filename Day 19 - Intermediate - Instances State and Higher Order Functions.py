def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

def calculator(n1,n2,func):  # Calculator is the higher order function that takes func as an input
    return func(n1,n2)

result = calculator(3,4,sub)

print(result)
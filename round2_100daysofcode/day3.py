#!/usr/bin/env python 

# This is about recursion and python algorithms

def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return recur_factorial(n - 1) * n


print(recur_factorial(5))

# permutations in python
# getting variations of things 

def permute(string, pocket=""):
    if len(string) == 0: 
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back 
            permute(together, letter + pocket)

print(permute("ABC", ""))
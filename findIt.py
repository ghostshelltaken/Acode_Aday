"""
Problem : Given the list of 1 to n. find the element which is missing from the list and find the repetitive element.

input: [1, 4, 4, 2, 5]
output: 4, 3
"""

import copy

def func(n, arr):
    base = []
    arr2 = copy.deepcopy(arr)   ##Shallow Copy

    for i in range(n):
        base.append(i+1)

    for i in arr:
        if i in base:
            base.remove(i)
            arr2.remove(i)

    print(base, arr2)


func(5, [1, 4, 4, 2, 5])
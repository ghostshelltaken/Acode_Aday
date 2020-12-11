"""
Problem: Given the inut string, return the string in reverse order.

input: "Rahul is a boy"
output: "boy a is Rahul"
"""


def reverseString(name):
    result = ""
    i, j = len(name), len(name)
    
    while i >= 0:
        if name[i-1] == " ":
            result = result + name[i:j] + " "
            # print(i, j)
            j = i - 1
            i = i - 1
        elif i == 0:
            result = result + name[i:j]
            j = i - 1
            i = i - 1
        else:
            i = i - 1

    print(result)
    return result

print(reverseString("Rahul is a boy") == "boy a is Rahul")
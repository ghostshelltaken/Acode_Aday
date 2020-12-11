"""
Problem:-
    Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second 
character of the final pair with an underscore ('_').

Examples:
    > ssolution('abc') # should return ['ab', 'c_']
    > solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
def solution(s):
    temp = ""
    res = []
    for i in s:
        temp = temp + i
        if len(temp)==2:
            res.append(temp)
            temp = ""
            
    if temp:
        temp = temp + "_"
        res.append(temp)
        return res
    else:
        return res
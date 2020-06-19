'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if len(word) < 2: #checks that we are at the end of string
        return 0
    if word[:2] == 'th': #increases count if 'th' is at front, and then calls with front character taken off
        return 1 + count_th(word[1:])
    return 0 + count_th(word[1:]) #if 'th' not found, calls without incrementing counter
    
    #Input string

    #output int of occurences

    #similar to cookies I think I need to have two base cases evaluating for 'th'. One that returns 0, and one that returns 1. Then a recursive case that moves towards those by calling the function with a progressed portion of the string.

    #need to eval for len of less than 2

    #start at beginning, eval first 2, check, call with removed character


    
    #No mention of how long it can be, but test cases are relatively short, so may not need to optimize to much.





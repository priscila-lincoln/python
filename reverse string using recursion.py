def reverseString(s): 
    if len(s) == 0:
        return
    temp = s[0]
    reverseString(s[1:])
    print(temp, end='')

s1 = ["h","e","l","l","o"]
reverseString(s1)

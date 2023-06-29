# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def valid_palindrome(s):
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    l = 0
    r = len(s)-1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))

def valid_palindrome2(s):
    #Time complexity: O(n)
    #Space complexity: O(n)

    test = ''
    for i in s:
        if i.isalnum():
            test += i.lower()
    return test == test[::-1]

print(valid_palindrome2("A man, a plan, a canal: Panama"))
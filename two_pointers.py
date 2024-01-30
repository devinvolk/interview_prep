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

# Find the minimum number of groups who's sum of each group is at max 3, and every element must be in a group.
# Given an Array like: [1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]
# return the minimum number of groups, in this case it would be 5 groups: (1.01 , 1.99), (1.01, 1.7), (3.0), (2.7), (2.3)
# Constraint: all elements are between 1.01-3 inclucsive, and each groups sum is at max 3

def efficient_janitor(lst):
    lst.sort(reverse=True)
    l, r = 0, len(lst)-1
    used_idx = set()
    groups = 0

    while l <= r:
        sum = lst[l]
        used_idx.add(l)
        while l < r and sum + lst[r] <= 3 and r not in used_idx:
            sum += lst[r]
            used_idx.add(r)
            r -= 1
        l += 1
        groups += 1
    
    return groups

print(efficient_janitor([1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]))
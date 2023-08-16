# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def valid_parentheses(s):
    #Time complexity: O(n)
    #Space complexty:O(n) 

    key = {')':'(', '}': '{', ']': '['}
    stack = []
    for i in s:
        if i not in key:
            stack.append(i)
            continue
        if not stack or stack[-1] != key[i]:
            return False
        stack.pop()
    return not stack

print(valid_parentheses("()[]{}"))

# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

def daily_temp(temperatures):
    #Time complexity: O(n)
    #Space complexity: O(n)
    stack = []
    res = [0]*len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res

print(daily_temp([73,74,75,71,69,72,76,73]))
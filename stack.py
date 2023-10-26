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

# 150. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

def rev_polish(tokens):
    #Time Complexity: O(n)
    #Space Complexity: O(n)

    stack = []

    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y-x)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y/x))
        else:
            stack.append(int(i))
    return stack[0]

print(rev_polish(["4","13","5","/","+"]))
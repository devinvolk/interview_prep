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
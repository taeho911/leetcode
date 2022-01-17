# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        open_ls = ['(', '{', '[']
        close_ls = [')', '}', ']']
        stack = []
        for char in s:
            if char in open_ls:
                stack.append(char)
            elif char in close_ls:
                if len(stack) == 0:
                    return False
                open_char = stack.pop()
                if open_char == '(' and char != ')' or \
                    open_char == '{' and char != '}' or \
                    open_char == '[' and char != ']':
                    return False
            else:
                return False
        return True if len(stack) == 0 else False

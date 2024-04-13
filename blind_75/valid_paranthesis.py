# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
def valid_paranthesis(s):
    stk = []
    for each_s in s:
        if each_s in ('(', '{', '['):
            stk.append(each_s)
        else:
            if len(stk) == 0:
                return False       
            lc = stk.pop()
            if each_s == ")" and lc != "(":
                return False
            if each_s == "}" and lc != "{":
                return False
            if each_s == "]" and lc != "[":
                return False
    return True

print(valid_paranthesis("()"))
print(valid_paranthesis("()[]{}"))
print(valid_paranthesis("(]"))

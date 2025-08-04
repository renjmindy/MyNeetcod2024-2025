class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = list()

        for r in range(len(s)):
            if s[r] == ')' and stack and stack[-1] == '(': stack.pop()
            else: stack.append(s[r])

        return len(stack)

class Solution:
    def calculate(self, s: str) -> int:
        
        stack = list()

        sign, num = 1, 0

        ans = 0

        stack.append(sign)

        for c in s:
            if c.isdigit(): num = num * 10 + int(c)
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c in ('+', '-'):
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0

        return ans + sign * num

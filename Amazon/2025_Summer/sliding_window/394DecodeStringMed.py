class Solution:
    def decodeString(self, s: str) -> str:
        
        num = 0
        stack = list()
        ans = ''

        for c in s:
            if c.isdigit(): num = num * 10 + int(c)
            elif c == '[':
                stack.append(num)
                stack.append(ans) # push old string into stack
                num = 0
                ans = ''
            elif c == ']':
                pre = stack.pop() # pop old string
                cnt = stack.pop()
                ans = pre + ans * cnt # pop old string + new char
            else:
                ans += c

        return ans

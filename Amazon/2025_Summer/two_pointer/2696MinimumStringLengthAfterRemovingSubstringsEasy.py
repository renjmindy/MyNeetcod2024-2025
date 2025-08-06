class Solution:
    def minLength(self, s: str) -> int:
        
        stack = list()

        ans = 0

        for c in s:
            found = False
            while not found and stack and ((stack[-1] == 'A' and c == 'B') or (stack[-1] == 'C' and c == 'D')):
                #print(stack)
                found = True
                stack.pop()
            
            if not found: stack.append(c)

        return len(''.join(stack))

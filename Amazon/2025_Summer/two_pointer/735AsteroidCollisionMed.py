class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = list()

        for r in range(len(asteroids)):
            col = False
            while stack and stack[-1] > 0 and asteroids[r] < 0:
                if stack[-1] > abs(asteroids[r]): col = True; break
                if stack[-1] == abs(asteroids[r]): col = True; stack.pop(); break
                if stack[-1] < abs(asteroids[r]): stack.pop()
            
            if not col: stack.append(asteroids[r])

        return stack

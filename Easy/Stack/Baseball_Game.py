class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        ans = list()

        for operation in operations:
            print(ans)
            if operation == 'C': ans.pop()
            elif operation == 'D': ans.append(ans[-1] * 2)
            elif operation == '+': ans.append(sum(ans[-2:]))
            else: ans.append(int(operation))

        return sum(ans)

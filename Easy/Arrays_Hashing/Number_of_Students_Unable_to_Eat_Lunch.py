class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        cp = Counter(students)

        for sandwich in sandwiches:
            if cp[sandwich]: cp[sandwich] -= 1
            else: return cp.total()

        return 0

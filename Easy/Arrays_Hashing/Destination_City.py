class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        ins = set(path[0] for path in paths)
        ous = set(path[1] for path in paths)

        return (ous - ins).pop()

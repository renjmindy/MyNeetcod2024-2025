class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        ans = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                neighbors = []
                for x in range(max(0, i - 1), min(len(img), i + 2)):
                    for y in range(max(0, j - 1), min(len(img[0]), j + 2)):
                        neighbors.append(img[x][y])
                print(neighbors)
                ans[i][j] = sum(neighbors) // len(neighbors)

        return ans

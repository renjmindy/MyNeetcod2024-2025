class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        ans = list()
        products.sort()

        for r in range(len(searchWord)):
            products = [product for product in products if product.startswith(searchWord[:r + 1])]
            ans.append(products[:3])

        return ans

class Solution:
    def maxProduct(self, s: str) -> int:
        def dp(i, first_sub, second_sub):
            if i == len(s):
                if first_sub == first_sub[::-1] and second_sub == second_sub[::-1]:
                    return len(first_sub) * len(second_sub)
                return -inf

            return max(
                dp(i + 1, first_sub + s[i], second_sub),
                dp(i + 1, first_sub, second_sub + s[i]),
                dp(i + 1, first_sub, second_sub)
            )

        return dp(0, "", "")

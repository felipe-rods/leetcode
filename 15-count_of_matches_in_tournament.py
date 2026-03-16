class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            ref = n // 2
            matches += ref
            n -= ref
        return matches


solution = Solution()
print(solution.numberOfMatches(385))
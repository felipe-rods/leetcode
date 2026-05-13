class Solution:
    def LengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])


solution = Solution()
print(solution.LengthOfLastWord('Eu amo a Wizards'))
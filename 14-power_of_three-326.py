class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            n /= 3
        return n == 1


solution = Solution()
print(solution.isPowerOfThree(27))
print(solution.isPowerOfThree(81))
print(solution.isPowerOfThree(243))
print(solution.isPowerOfThree(3))
print(solution.isPowerOfThree(6))
print(solution.isPowerOfThree(1))
print(solution.isPowerOfThree(9))

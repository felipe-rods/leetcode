class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1


solution = Solution()
print(solution.isPowerOfFour(4))
print(solution.isPowerOfFour(3))
print(solution.isPowerOfFour(8))
print(solution.isPowerOfFour(16))
print(solution.isPowerOfFour(128))
print(solution.isPowerOfFour(1024))

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 2:
            n /= 2
        return True if n == 2 or n == 1 else False

solution = Solution()
print(solution.isPowerOfTwo(2))
print(solution.isPowerOfTwo(3))
print(solution.isPowerOfTwo(4))
print(solution.isPowerOfTwo(1))
print(solution.isPowerOfTwo(8))
print(solution.isPowerOfTwo(6))
print(solution.isPowerOfTwo(16))
print(solution.isPowerOfTwo(32))

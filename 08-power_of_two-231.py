class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0

solution = Solution()
print(solution.isPowerOfTwo(2))
print(solution.isPowerOfTwo(3))
print(solution.isPowerOfTwo(4))
print(solution.isPowerOfTwo(1))
print(solution.isPowerOfTwo(8))
print(solution.isPowerOfTwo(6))
print(solution.isPowerOfTwo(16))
print(solution.isPowerOfTwo(32))

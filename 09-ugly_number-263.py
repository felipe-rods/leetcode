class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1


solution = Solution()
print(solution.isUgly(6))
print(solution.isUgly(1))
print(solution.isUgly(14))
print(solution.isUgly(7))
print(solution.isUgly(8))
print(solution.isUgly(9))
print(solution.isUgly(17))
print(solution.isUgly(15))
        
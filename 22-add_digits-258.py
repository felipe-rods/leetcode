class Solution:
    def add_digits(self, num: int) -> int:
        while num > 9:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num



solution = Solution()
print(solution.add_digits(38))
print(solution.add_digits(9))
print(solution.add_digits(14))
print(solution.add_digits(1234))
print(solution.add_digits(6534))
print(solution.add_digits(777))

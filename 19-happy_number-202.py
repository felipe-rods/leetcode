class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = []
        digit = 0
        while n != 1:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            if total in numbers:
                return False
            numbers.append(total)
            n = total
        return True


solution = Solution()
print(solution.isHappy(1))
print(solution.isHappy(70))
print(solution.isHappy(10))
print(solution.isHappy(13))
print(solution.isHappy(49))
print(solution.isHappy(97))
print(solution.isHappy(28))
print(solution.isHappy(86))
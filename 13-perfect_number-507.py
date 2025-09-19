class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += (num // i)
        return sum == num

        
                

solution = Solution()
print(solution.checkPerfectNumber(28))
print(solution.checkPerfectNumber(6))
print(solution.checkPerfectNumber(25))
print(solution.checkPerfectNumber(64))

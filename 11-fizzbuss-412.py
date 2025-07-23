class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        fizz = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                fizz.append('FizzBuzz')
            elif i % 3 == 0:
                fizz.append('Fizz')
            elif i % 5 == 0:
                fizz.append('Buzz')
            else:
                fizz.append(str(i))
        return fizz


solution = Solution()
print(solution.fizzBuzz(15))
print(solution.fizzBuzz(25))
print(solution.fizzBuzz(7))

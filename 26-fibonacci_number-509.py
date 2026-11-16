# recursão
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

# sem recursão
class Solution2:
    def fib(self, n: int) -> int:
        fib_list = [0, 1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            while len(fib_list) <= n:
                next_fib = fib_list[-1] + fib_list[-2]
                fib_list.append(next_fib)
        return fib_list
                

solution = Solution()
solution2 = Solution2()
print(solution2.fib(200))



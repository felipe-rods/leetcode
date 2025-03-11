class Solution(object):
    def majorityElement(self, nums):
        number = None
        count = 0
        for num in nums:
            if count == 0:
                number = num
            count += (1 if num == number else - 1)

        return number


solution = Solution()
print(solution.majorityElement([1, 1, 1, 2]))
print(solution.majorityElement([6, 5, 5, 6, 3, 5]))

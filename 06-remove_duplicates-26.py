class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        unique_elements = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[unique_elements] = nums[index]
                unique_elements += 1

        return unique_elements
                

solution = Solution()
print(solution.removeDuplicates([1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 8, 8, 9]))
print(solution.removeDuplicates([1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 8, 8, 9, 10, 10, 11, 13, 13]))
print(solution.removeDuplicates([1, 1, 2, 3, 6, 8, 8, 9]))

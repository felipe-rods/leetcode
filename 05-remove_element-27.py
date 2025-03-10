class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        k = len(nums)

        return nums


solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
print(solution.removeElement([3, 3], 3))

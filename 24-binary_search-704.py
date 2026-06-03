class Solution:
    def binary_search(self, nums: list, target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            if target > nums[mid]:
                low = mid + 1
        return -1


solution = Solution()
print(solution.binary_search([-1, 0, 3, 5, 9, 12], 9))
print(solution.binary_search([-1, 0, 3, 5, 9, 12], 2))

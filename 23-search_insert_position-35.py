class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid + 1
            if target < nums[mid]:
                high = mid - 1
        return mid + 1 if target > nums[mid] else mid
        
        


solution = Solution()
print(solution.search_insert([1, 3, 5, 6], 5))
print(solution.search_insert([1, 3, 5, 6], 1))
print(solution.search_insert([1, 3, 5, 6], 3))
print(solution.search_insert([1, 3, 5, 6], 6))
print(solution.search_insert([1, 3, 5, 6], 2))
print(solution.search_insert([1, 3, 5, 6], 7))
print(solution.search_insert([1, 3, 5, 6], 0))
print(solution.search_insert([1, 3], 2))

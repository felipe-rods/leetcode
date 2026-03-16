class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pair_index = {}
        
        for index, num in enumerate(nums):
            if target - num in pair_index:
                return [index, pair_index[target - num]]
            pair_index[num] = index

                 
solution = Solution()
print(solution.twoSum([1, 2, 3, 6, 7], 5))

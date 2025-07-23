class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 2]))
print(solution.containsDuplicate([1, 3, 1]))
print(solution.containsDuplicate([1, 4, 3, 2]))
print(solution.containsDuplicate([2, 3]))

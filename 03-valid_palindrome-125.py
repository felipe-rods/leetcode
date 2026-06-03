class Solution(object):
    def isPalindrome(self, s):
        palindrome = [letter.lower() for letter in s if letter.isalnum()]
        left = 0
        right = len(palindrome) - 1
        while left < right:
            if palindrome[left] == palindrome[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(""))
print(solution.isPalindrome("Girafarig"))

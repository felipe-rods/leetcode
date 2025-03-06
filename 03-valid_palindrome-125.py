class Solution(object):
    def isPalindrome(self, s):
        palindrome = [letter.lower() for letter in s if letter.isalnum()]
        reversed_palindrome = palindrome[::-1]
        return True if palindrome == reversed_palindrome else False

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(""))
print(solution.isPalindrome("Girafarig"))

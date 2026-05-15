class Solution:
	def is_palindrome(self, number):
		if number < 0:
			return False
		else:
			temp = number
			reverse_number = 0

			while temp > 0:
				digit = temp % 10
				reverse_number = reverse_number * 10 + digit
				temp //= 10

			return reverse_number == number


solution = Solution()
print(solution.is_palindrome(1441))
print(solution.is_palindrome(-1441))
print(solution.is_palindrome(1234321))
print(solution.is_palindrome(6524))

class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        integer = 0
        previous_number = 0

        for letter in reversed(s):
            if roman_numerals[letter] >= previous_number:
                integer += roman_numerals[letter]
                previous_number = roman_numerals[letter]
            else:
                integer -= roman_numerals[letter]
        return integer

solution = Solution()
print(solution.romanToInt('MCDIX'))
print(solution.romanToInt('MCMDDDIXV'))
print(solution.romanToInt('XIV'))
print(solution.romanToInt('MMMCCCXXXIII'))
print(solution.romanToInt('CM'))

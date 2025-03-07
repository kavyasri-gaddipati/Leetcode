class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        result = []

        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return

            for letter in mapping[digits[index]]:
                backtrack(index + 1, current + letter)

        backtrack(0, "")
        return result

# Example Usage
digits = "23"
sol = Solution()
print(sol.letterCombinations(digits))

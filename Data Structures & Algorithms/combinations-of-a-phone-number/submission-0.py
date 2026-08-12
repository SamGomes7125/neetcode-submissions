class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
                return []
        letters = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                }
        index = 0
        current = ""
        result = []
        def recursion(index, current):    
            if index == len(digits):
                result.append(current)
                return
            for letter in letters[digits[index]]:
                recursion(index + 1, current + letter)
        recursion(0, "")
        return result







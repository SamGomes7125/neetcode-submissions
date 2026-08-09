class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = 0
        c = 0
        current = ""
        result = []
        def backtracking(current, o, c):
            if o == n and c == n:
                result.append(current)
                return 
            else:
                if o < n:
                    backtracking(current + "(", o + 1, c)

                if c < o:
                    backtracking(current + ")", o, c + 1)
        backtracking(current, o, c)
        return result

        
class Solution:
    def isValid(self, s: str) -> bool:

        l = True
        stack = []

        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        if len(s) % 2 != 0:
            l = False

        else:
            for i in range(len(s)):

                if s[i] not in pairs:
                    stack.append(s[i])

                else:

                    if stack and pairs[s[i]] == stack[-1]:
                        stack.pop()

                    else:
                        l = False
                        break

            if stack != []:
                l = False

        return l
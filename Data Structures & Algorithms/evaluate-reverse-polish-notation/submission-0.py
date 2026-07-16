class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for i in tokens:
            try:
                num = int(i)
                numbers.append(num)
            except:
                num1 = numbers.pop()
                num2 = numbers.pop()
                if i == "+":
                    numbers.append(num2+num1)
                elif i == "-":
                    numbers.append(num2-num1)
                elif i == "*":
                    numbers.append(num2*num1)
                else:
                    numbers.append(int(num2/num1))
        return numbers[0]
        
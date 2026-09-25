class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def doMath(numOne: int, numTwo: int, operator: str) -> int:
            match operator:
                case "+":
                    return numOne + numTwo
                case "-":
                    return numOne - numTwo
                case "*":
                    return numOne * numTwo
                case "/":
                    return int(numOne / numTwo)
                case _:
                    raise ValueError("shut up intellisense, i know the constraints")

        stack = []
        for t in tokens:
            match t:
                case "+" | "-" | "*" | "/":
                    numTwo = stack.pop(-1)
                    numOne = stack.pop(-1)
                    stack.append(doMath(numOne, numTwo, t))
                case _:
                    stack.append(int(t))

        return stack[0]

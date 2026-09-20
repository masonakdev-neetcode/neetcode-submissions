class MinStack:
    def __init__(self):
        self.__stack = []
        self.__minStack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        self.__minStack.append(min(val, self.__minStack[-1] if self.__minStack else val))

    def pop(self) -> None:
        self.__stack.pop(-1)
        self.__minStack.pop(-1)

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__minStack[-1]

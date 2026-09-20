import sys

class MinStack:
    __sysMaxSize = sys.maxsize

    def __init__(self):
        self.__stack = []
        self.__currMin = self.__sysMaxSize

    def push(self, val: int) -> None:
        self.__currMin = min(val, self.__currMin)
        self.__stack.append(val)

    def pop(self) -> None:
        if self.__stack:
            popped = self.__stack.pop(-1)
            if popped == self.__currMin:
                self.__resetCurrMin()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__currMin
    
    def __resetCurrMin(self) -> None:
        if not self.__stack:
            self.__currMin = self.__sysMaxSize
            return

        newMin = self.__sysMaxSize
        for e in self.__stack:
            newMin = min(e, newMin)
        
        self.__currMin = newMin

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__arr = [(0, False)] * self.__capacity
        self.__len = 0

    def get(self, i: int) -> int:
        return self.__arr[i][0]

    def set(self, i: int, n: int) -> None:
        if not self.__arr[i][1]:
            self.__len += 1
        self.__arr[i] = (n, True)

    def pushback(self, n: int) -> None:
        if self.__len == self.__capacity:
            self.resize()
        self.__arr[self.__len] = (n, True)
        self.__len += 1

    def popback(self) -> int:
        self.__len -= 1
        ans = self.__arr[self.__len][0]
        self.__arr[self.__len] = (-69, False)
        return ans

    def resize(self) -> None:
        tempArr = self.__arr.copy()
        self.__capacity *= 2
        self.__arr = [(-69, False)] * self.__capacity
        for i, num in enumerate(tempArr):
            self.__arr[i] = num

    def getSize(self) -> int:
        return self.__len
    
    def getCapacity(self) -> int:
        return self.__capacity

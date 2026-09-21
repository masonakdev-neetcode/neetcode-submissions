class Solution:
    # believe it or not, this is a 67 joke
    __beginElementDelimiter = "^"
    __endElementDelimiter = "&"

    # this is just the answer to life
    __beginCharDelimiter = "$"
    __endCharDelimiter = "@"

    # 420 joke but admittedly convoluted
    __emptyInput = ")"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.__emptyInput

        encoded = ""
        for s in strs:
            encoded += self.__beginElementDelimiter
            for c in s:
                encoded += self.__beginCharDelimiter
                encoded += str(ord(c))
                encoded += self.__endCharDelimiter
            encoded += self.__endElementDelimiter
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s or s == self.__emptyInput:
            return []

        decoded = []
        builder = ""

        n = len(s)
        ptr = 0
        while ptr < n:
            match s[ptr]:
                case self.__beginElementDelimiter:
                    ptr += 1

                case self.__endElementDelimiter:
                    decoded.append(builder)
                    builder = ""
                    ptr += 1

                case self.__beginCharDelimiter:
                    ptr += 1
                    ordBuilder = ""
                    while ptr < n and s[ptr] != self.__endCharDelimiter:
                        ordBuilder += s[ptr]
                        ptr += 1

                    if ordBuilder != "":
                        ordBuilder = chr(int(ordBuilder))
                    builder += ordBuilder

                case self.__endCharDelimiter:
                    ptr += 1

        return decoded

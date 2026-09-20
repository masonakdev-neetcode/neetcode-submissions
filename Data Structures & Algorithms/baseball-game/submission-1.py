class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, ans = [], 0
        for op in operations:
            match op:
                case "+":
                    ans += record[-1] + record[-2]
                    record.append(record[-1] + record[-2])
                case "D":
                    ans += record[-1] *2
                    record.append(record[-1] * 2)
                case "C":
                    ans -= record.pop()
                case _:
                    rawScore = int(op)
                    ans += rawScore
                    record.append(rawScore)
        
        return ans

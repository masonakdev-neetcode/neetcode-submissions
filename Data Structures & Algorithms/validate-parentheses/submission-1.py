class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for c in s:
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]:
                    return False
                continue
            stack.append(c)
        
        return not stack

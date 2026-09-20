class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        
        charFreq = [0] * 26
        for i in range(n):
            charFreq[ord(s[i]) - ord('a')] += 1
            charFreq[ord(t[i]) - ord('a')] -= 1
        
        for freq in charFreq:
            if freq != 0:
                return False
        
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n_s = len(s)
        n_t = len(t)
        if n_s != n_t:
            return False
        
        charCount = dict()
        for c in s:
            if c not in charCount:
                charCount[c] = 1
            else:
                charCount[c] += 1
        
        for c in t:
            if c not in charCount or charCount[c] == 0:
                return False
            charCount[c] -= 1
        
        return True
        
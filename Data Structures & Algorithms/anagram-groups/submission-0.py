class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charFreq = [0] * 26
        # k: charMap, v: list of words
        charFreqToWords = dict()
        for word in strs:
            wordCharFreq = charFreq.copy()
            for char in word:
                wordCharFreq[ord(char) - ord('a')] += 1
            wordCharFreq = tuple(wordCharFreq)
            if wordCharFreq not in charFreqToWords:
                charFreqToWords[wordCharFreq] = list()
            charFreqToWords[wordCharFreq].append(word)

        return list(charFreqToWords.values())

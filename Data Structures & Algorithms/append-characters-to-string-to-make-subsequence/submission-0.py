class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPointer = 0
        tPointer = 0
        subsequenceString = ""

        while sPointer < len(s) and tPointer < len(t):
            if t[tPointer] == s[sPointer]:
                 subsequenceString += t[tPointer]
                 tPointer += 1
            sPointer += 1
        if subsequenceString == t:
            return 0
        else:
            return len(t) - tPointer
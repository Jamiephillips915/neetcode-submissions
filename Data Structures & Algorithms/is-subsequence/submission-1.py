class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        output = ""
        headT = 0
        i = 0
        while i < len(s) and headT < len(t):
            if s[i] == t[headT]:
                output += s[i]
                i += 1
            headT += 1
        if output == s:
            return True
        else:
            return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        total = 0
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in hashmap:
                    hashmap[s[i]] = hashmap[s[i]] + 1
                else:
                    hashmap[s[i]] = 1
            print(hashmap)
            for i in range(len(t)):
                if t[i] in hashmap:
                    hashmap[t[i]] -= 1
                else:
                    return False
            print(hashmap.values())
            for i in hashmap.values():
                if i != 0:
                    return False
            return True
            
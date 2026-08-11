class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = {}
        c2 = {}
        if (len(s) != len(t)):
            return False
        for ch in s:
            c1[ch] = c1.get(ch, 0) + 1
        for ch in t:
            if ch not in c1:
                return False
            c2[ch] = c2.get(ch, 0) + 1
        return c1 == c2
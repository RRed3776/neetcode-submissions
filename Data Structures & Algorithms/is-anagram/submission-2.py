class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = {}
        c2 = {}
        for ch in s:
            c1[ch] = c1.get(ch, 0) + 1
        for ch in t:
            c2[ch] = c2.get(ch, 0) + 1
        return c1 == c2
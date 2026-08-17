class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len = 0, 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1      
            charSet.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len
                    
        
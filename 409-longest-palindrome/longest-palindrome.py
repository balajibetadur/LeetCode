class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        for ch in s: hash[ch] = hash.get(ch, 0) + 1

        res = 0

        for ch, count in hash.items(): 
            res += (count // 2) * 2
            if res % 2 == 0 and count % 2 == 1: res += 1

        return res
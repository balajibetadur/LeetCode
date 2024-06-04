class Solution:
    def longestPalindrome(self, s: str) -> int:
        # approach 1
        # hash = {}
        # for ch in s: hash[ch] = hash.get(ch, 0) + 1
        # res = 0
        # for ch, count in hash.items(): 
        #     res += (count // 2) * 2
        #     if res % 2 == 0 and count % 2 == 1: res += 1
        # return res

        #approach 2
        temp = []
        for ch in s:
            if ch in temp: temp.remove(ch)
            else: temp.append(ch)

        if len(temp) == 0: return len(s)
        else: return len(s) - len(temp) + 1
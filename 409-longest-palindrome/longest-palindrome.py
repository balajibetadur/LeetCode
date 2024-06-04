# 1. Approach
# a. Get count of all characters in hash and all all counts using (count // 2) * 2, and add 1 at the end if res < len(s), we can also add val - 1 incase of odd nums as  2nd sub approach
# Add element in list and when you encounter it again remove it, at the end if list is empty retrun len(s) else return len(s) - len(list) + 1
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # approach 1
        hash = {}
        for ch in s: hash[ch] = hash.get(ch, 0) + 1
        res = 0
        for ch, count in hash.items(): 
            res += (count // 2) * 2
            if res % 2 == 0 and count % 2 == 1: res += 1 
            # approach 1.2 - cal also append count - 1 and 
            # append 1 at end if len(res) < len(s)
        return res

        #approach 2
        # temp = []
        # for ch in s:
        #     if ch in temp: temp.remove(ch)
        #     else: temp.append(ch)

        # if len(temp) == 0: return len(s)
        # else: return len(s) - len(temp) + 1
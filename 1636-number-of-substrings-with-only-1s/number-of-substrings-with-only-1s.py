class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        count_one = 0
        for ch in s:
            if ch == '0': 
                count += ((count_one * (count_one + 1)) / 2) % (10 ** 9 + 7)
                count_one = 0
            else: count_one += 1
        count += ((count_one * (count_one + 1)) / 2) % (10 ** 9 + 7)
        return int(count)
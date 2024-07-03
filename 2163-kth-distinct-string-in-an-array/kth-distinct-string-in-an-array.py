class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash = {}
        for ch in arr: hash[ch] = hash.get(ch, 0) + 1
        counter = 0
        print(hash)
        for ch in arr:
            if hash[ch] == 1: counter += 1
            if counter == k: return ch
        return ''
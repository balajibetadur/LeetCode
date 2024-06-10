class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freq_array = [0] * 101
        for height in heights: freq_array[height] += 1

        res, index = 0, 0
        for height in heights:
            while freq_array[index] == 0: index += 1
            if index != height: res += 1
            freq_array[index] -= 1
        return res
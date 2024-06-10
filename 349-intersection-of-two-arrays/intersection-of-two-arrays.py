class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_freq = [0] * 1001
        for num in nums1: nums1_freq[num] = 1

        res = []
        for num in nums2:
            if nums1_freq[num]:
                res.append(num)
                nums1_freq[num] -= 1

        return res

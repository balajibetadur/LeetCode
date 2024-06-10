class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_map = {}
        stack = []

        for num in nums2:
            while stack != [] and stack[-1] < num:
                max_map[stack[-1]] = num
                stack.pop()
            stack.append(num)

        return [max_map.get(num, -1) for num in nums1]

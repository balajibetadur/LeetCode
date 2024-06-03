class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        for num in nums:
            res.append(pre)
            pre *= num 

        post = 1
        n = len(res)
        for i in range(n):
            res[n - i - 1] *= post
            post *= nums[n - i - 1]


        return res


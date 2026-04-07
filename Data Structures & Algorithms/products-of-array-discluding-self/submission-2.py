class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        # find the prefix product of all left elements
        prefix = 1
        for i in range(len(nums)):
            # multipying to get the ith product
            res[i] = prefix
            prefix *= nums[i]
        # find the suffix product of all right elements
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            # multipying to get the ith product
            res[i] *= postfix
            postfix *= nums[i]
        # return
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find the prefix product of all left elements
        left, curr_prod = [0]*len(nums), 1
        for i in range(0, len(nums)):
            left[i] = curr_prod
            curr_prod *= nums[i]
        
        # find the suffix product of all right elements
        right, curr_prod = [0]*len(nums), 1
        for i in range(len(nums)-1, -1, -1):
            right[i] = curr_prod
            curr_prod *= nums[i]
        
        # multipying to get the ith product
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        # return
        return res
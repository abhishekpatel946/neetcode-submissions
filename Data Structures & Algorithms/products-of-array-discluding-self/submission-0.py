class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(0, len(nums)):
            total_product = 1
            for j in range(0, len(nums)):
                if i == j: continue
                total_product *= nums[j]
            result[i] = total_product
        return result
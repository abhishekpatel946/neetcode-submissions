class Solution:
    def brute(self, nums: List[int], target: int) -> List[int]:
        # TC = o(n^2), SC = o(1)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.brute(nums, target)
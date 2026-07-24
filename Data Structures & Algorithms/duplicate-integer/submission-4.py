class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Sort the nums array
        nums.sort()
        print(nums)

        # 2. Base case
        if not len(nums) > 1:
            return False
        
        # 3. Find the left-right match
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1
        
        # 4. Return
        return False
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # computation
        start, end = 0, len(nums)
        while start != end:
            nums.append(nums[start])
            start += 1
        
        # return
        return nums
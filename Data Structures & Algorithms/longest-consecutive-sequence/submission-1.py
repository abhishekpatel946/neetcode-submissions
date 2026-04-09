class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 0:
            return 0
        # iteration
        nums_set, longest = list(set(nums)), 1
        for i in range(len(nums_set)):
            if nums_set[i] - 1 not in nums_set:
                x = nums_set[i]
                count = 0
                while x in nums_set:
                    count += 1
                    x += 1
                longest = max(count, longest)
        return longest
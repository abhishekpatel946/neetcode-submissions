from collections import Counter

class Solution:
    def brute(self, nums: List[int]) -> bool:
        # TC = o(n^2), SC = o(1)
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def better(self, nums: List[int]) -> bool:
        # TC = O(n), SC = (n)
        hashmap = Counter(nums)
        for k, v in hashmap.items():
            if v > 1:
                return True
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.better(nums)


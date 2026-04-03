class Solution:
    def brute(self, nums: List[int], target: int) -> List[int]:
        # TC = o(n^2), SC = o(1)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def better(self, nums: List[int], target: int) -> List[int]:
        # TC = o(n), SC = o(n)
        # precomputed hashmap
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        # get the k element from hashmap if available
        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashmap and hashmap[k] != i:
                return [i, hashmap[k]]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.better(nums, target)
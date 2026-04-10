class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()

        # find triplets
        result = []
        for i in range(len(nums)):
            # using 2sum
            left, right = i + 1, len(nums) - 1
            while left < right:
                x = nums[i] + nums[left] + nums[right]
                if x == 0:
                    tmp = sorted([nums[i], nums[left], nums[right]])
                    if tmp not in result: 
                        result.append(tmp)
                    left += 1
                    right -= 1
                elif x < 0:
                    left += 1
                else:
                    right -= 1
        # return
        return result
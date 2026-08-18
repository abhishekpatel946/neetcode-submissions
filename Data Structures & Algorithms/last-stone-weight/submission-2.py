class Solution:
    def maximumStone(self, stones: List[int]) -> List[int]:
        first, second = -1, -2
        for stone in stones:
            if stone >= first:
                second = first
                first = stone
            elif stone >= second and stone < first:
                second = stone
        return [first, second]

    def lastStoneWeight(self, stones: List[int]) -> int:
        # base case
        if len(stones) <= 1:
            return stones[0]
        
        # crush them togather
        while len(stones) > 1:
            # get the first & second max elements from stones array
            first_max, second_max = self.maximumStone(stones)
            
            # remove them from array
            stones.remove(first_max)
            stones.remove(second_max)

            # calculation
            if first_max == second_max:
                stones.append(0) # coz both crush togather and becomes 0
            else:
                remaining_stones = first_max - second_max
                stones.append(remaining_stones)

        # return (once the array has only single value/stone left)
        return stones[0]
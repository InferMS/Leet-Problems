from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        # Build the hash table
        for i in range(len(nums)):
            numIndex[nums[i]] = i

        # Find the complement
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numIndex and numIndex[complement] != i:
                return [i, numIndex[complement]]

        return []  # No solution found
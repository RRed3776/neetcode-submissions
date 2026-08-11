class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            d[val] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d and d[diff] != i:
                return [i, d[diff]]
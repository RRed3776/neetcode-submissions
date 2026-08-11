class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            d[val] = i
       
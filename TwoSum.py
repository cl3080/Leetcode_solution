class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,b in enumerate(nums):
            rest = target - b
            if rest in nums and nums.index(rest)!= i:
                return [i,nums.index(rest)]




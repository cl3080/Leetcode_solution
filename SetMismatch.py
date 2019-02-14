class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        hashs = [0]*len(nums)
        for i in range(len(nums)):
            hashs[nums[i]-1] += 1
        return [hashs.index(2)+1,hashs.index(0)+1]

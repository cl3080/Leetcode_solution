# solution 1: 
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        
        for num in nums:
            counts[num] += 1
            
        i = 0
        
        for j in range(3):
            for _ in range(counts[j]):
                nums[i] = j
                i=i + 1


# solution 2:
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size-1):
            for j in range(i+1,size):
                if nums[j]< nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

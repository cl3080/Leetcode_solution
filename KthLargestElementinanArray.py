class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        nums.sort()
        reverse_nums = nums[::-1]
        return reverse_nums[k-1]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i<k:
            num = nums.pop()
            nums.insert(0,num)
            i = i+1

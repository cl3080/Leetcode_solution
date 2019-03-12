class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        size = len(nums)
        
        left = 1
        for i in range(size-1):
            left = left * nums[i]
            ans[i+1] = ans[i+1]*left
        
        right = 1
        for i in range(size-1,0,-1):
            right = right * nums[i]
            ans[i-1] = ans[i-1] * right
        
        return ans

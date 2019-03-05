class Solution:
    def search(self, nums: List[int], target: int) -> int:
       # for i,x in enumerate(nums):
       #     if x == target:
       #         return i
       # return -1
        low = 0
        high = len(nums)
        while high != low:
            mid = (high + low)//2
            if nums[mid] == target: return mid
            if nums[mid] > nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = low + 1
            else:
                if target > nums[mid] and target <= nums[high-1]:
                    low = mid + 1         
                else:
                    high = mid
        return -1

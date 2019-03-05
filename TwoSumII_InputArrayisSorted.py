class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)  
        left, right = 0,size-1
        
        for i in range(size):
            while left<right:
                total = numbers[left] + numbers[right]
                if total < target:
                    left = left + 1
                if total > target:
                    right = right -1
                if total == target:
                    return left+1,right+1
                

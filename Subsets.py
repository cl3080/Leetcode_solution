class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth,start,numberList):
            res.append(numberList)
            if depth == len(nums): return 
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,numberList+[nums[i]])
        
        res = []
        dfs(0,0,[])
    
        return res

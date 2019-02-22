class Solution:
    def numSubarrayBoundedMax(self, A: 'List[int]', L: 'int', R: 'int') -> 'int':
        ans = 0
        lastIndex = 0
        A = A + [10**10]
        for i,x in enumerate(A):
            if x > R:
                ans = ans + self.numSubarrayMinMax(A[lastIndex:i],L)
                lastIndex = i + 1
        return ans
    
    def numSubarrayMinMax(self, A:'List[int]',L:'int') -> 'int':
        ans = 0
        lastIndex = 0
        for i, x in enumerate(A):
            if x >= L:
                ans = ans + (i-lastIndex+1)*(len(A)-i)
                lastIndex = i+1
        return ans

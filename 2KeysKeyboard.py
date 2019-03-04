class Solution:
    def minSteps(self, n: int) -> int:
        if n==1: return 0
        step = 0
        for i in range(2,n+1):
            while n%i == 0:
                step = step + i
                n = n//i
        return step

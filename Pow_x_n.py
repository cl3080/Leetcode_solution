class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0: return 1.0
        if n<0: return self.myPow(1/x,-n)
        elif n%2 == 1:
            return x*self.myPow(x*x,n//2)
        else:
            return self.myPow(x*x,n//2)

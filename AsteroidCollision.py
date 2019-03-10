class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            while stack and aster<0 and stack[-1]>0:
                pre = stack.pop()
                if pre == -aster:
                    aster = None
                    break
                elif pre > -1*aster:
                    aster = pre
            if aster != None:
                stack.append(aster) 
        return stack
            

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [-1]*len(A)
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b,i) for i, b in enumerate(B)))
        
        for i in range(len(A)):
            a = A.popleft()
            b = B[0]
            
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
                
            res[b[1]] = a
            
        return res
        

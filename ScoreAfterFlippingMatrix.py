class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if len(A) == 0 or len(A[0]) == 0:
            return 0
        
        for i in range(len(A)):
            if A[i][0] == 1:
                continue
            else:
                for j in range(len(A[i])):
                    if A[i][j] == 1:
                        A[i][j] = 0
                    else:
                        A[i][j] = 1
        row = len(A)
        column = len(A[0])
        
        for i in range(column):
            counts_0 = 0
            counts_1 = 0
            for j in range(row):
                if A[j][i] == 0:
                    counts_0 = counts_0 + 1
                else:
                    counts_1 = counts_1 + 1
            if counts_0 > counts_1:
                for j in range(row):
                    if A[j][i] == 0:
                        A[j][i] = 1
                    else:
                        A[j][i] = 0
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                power = column - j - 1
                ans = A[i][j]*2**power + ans
                
        return ans

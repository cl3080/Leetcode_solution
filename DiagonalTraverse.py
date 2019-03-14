class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix or not matrix[0]: return []
        
        ans = []
        M = len(matrix)
        N = len(matrix[0])
        r = c = 0
        
        
        for i in range(M*N):
            ans.append(matrix[r][c])
            if ((r+c)%2 == 1):
                if (r == M-1): c = c + 1
                else: 
                    if (c == 0): r = r + 1
                    else:
                        r = r + 1
                        c = c -1
            else:
                if (c == N-1): r = r + 1
                else:
                    if (r == 0): c = c + 1
                    else:
                        r = r - 1
                        c = c + 1
 
        return ans

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False   
        rows = len(matrix)
        columns = len(matrix[0])
        if rows == 0 or columns == 0: return False
        
        for i in range(rows):
            head = min(matrix[i])
            tail = max(matrix[i])
            if target > tail: 
                continue
            else:
                for j in range(columns):
                    if target == matrix[i][j]:
                        return True
        return False

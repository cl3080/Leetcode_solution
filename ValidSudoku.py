class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        def isValid(x,y,tmp):
            for i in range(9):
                if board[i][y] == tmp: return False 
            for j in range(9):
                if board[x][j] == tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3)*3+i][(y//3)*3+j] == tmp:
                        return False
            return True
        
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.': continue
                
                tmp = board[x][y]
                board[x][y] = 'A'
                
                if isValid(x,y,tmp) == False: return False
                else:
                    board[x][y] = tmp
                    
        return True

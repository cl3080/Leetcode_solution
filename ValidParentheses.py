class Solution:
    def isValid(self, s: 'str') -> 'bool':
        
        par = [None]
        par_dic = {')':'(','}':'{',']':'['}
        
        for c in s:
            if c in par_dic and par_dic[c] == par[len(par)-1]:
                par.pop()
            else:
                par.append(c)
            
        return len(par) == 1

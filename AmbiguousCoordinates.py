class Solution:
    def ambiguousCoordinates(self, S: 'str') -> 'List[str]':
        S = S[1:-1]
        size = len(S)
        ans = []
        for i in range(1,len(S)):
            left,right = S[:i],S[i:]
            first_number = self.Valid(left)
            second_number = self.Valid(right)
            if first_number and second_number:
                for i in first_number:
                    for j in second_number:
                        ans.append('('+str(i)+', '+str(j)+')')     
        return ans
        
    def Valid(self,num):
        number_list = []
        if len(num) == 1 or num[0] != '0':
            number_list.append(num)
        for i in range(1,len(num)):
            integer,factor = num[:i],num[i:]
            if (integer[0] == '0' and len(integer) > 1) or factor[-1] == '0':
                continue
            number_list.append(integer+'.'+factor)
        return number_list
            
        

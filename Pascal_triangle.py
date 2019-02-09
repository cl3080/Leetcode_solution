class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        triangle = []
        count = 1
        temp = [1]
        while count<=numRows:
            triangle.append(temp)
            new_temp=[1]
            for i in range(count-1):
                number = temp[i] + temp[i+1]
                new_temp.append(number)
            new_temp.append(1)
            temp = new_temp
            count = count + 1
            
        return triangle

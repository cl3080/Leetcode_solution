class Solution:
    def constructRectangle(self, area: 'int') -> 'List[int]':
        import math
        side = int(math.sqrt(area))
        if side*side == area:
            return [side,side]
        else:
            for i in range(side+1):
                W = side-i
                L = area/W
                if L == int(area/W):
                    return ([int(L),W])

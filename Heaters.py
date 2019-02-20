class Solution:
    def findRadius(self, houses: 'List[int]', heaters: 'List[int]') -> 'int':
        houses.sort()
        heaters.sort()
        
        heaters = [float('-inf')] + heaters + [float('inf')]
        
        r = i = 0
        
        for j in range(len(houses)):
            while houses[j] > heaters[i+1]:
                i = i + 1
            dist = min(houses[j]-heaters[i],heaters[i+1]-houses[j])
            r = max(r,dist)
        return r            
        

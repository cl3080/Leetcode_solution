class Solution:
    def numRescueBoats(self, people: 'List[int]', limit: 'int') -> 'int':
        people.sort()
        boat = 0
        high = len(people)-1
        low = 0
        
        while high >= low:
            if (people[high] + people[low] ) <= limit:
                low = low + 1
            high = high -1
            boat = boat + 1
            
        return boat

class Solution:
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
        
        N = len(gas)
        if sum(gas) < sum(cost):
            return -1
        
        diff = 0
        station = 0
        
        for i in range(N):
            if gas[i] + diff < cost[i]:
                station = i+1
                diff = 0
            else:
                diff = diff + gas[i] - cost[i]
        
        return station
                

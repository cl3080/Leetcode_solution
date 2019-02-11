class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        candidate = [1]*len(primes)
        ids = [0]*len(primes)
        ugly_numbers = [1]
        Mins = 1
        
        for count in range(1,n):
            for i in range(len(primes)):
                if Mins == candidate[i]:
                    candidate[i] = primes[i]*ugly_numbers[ids[i]]
                    ids[i] = ids[i] + 1
            Mins = min(candidate)
            ugly_numbers.append(Mins)
            
        return ugly_numbers.pop()

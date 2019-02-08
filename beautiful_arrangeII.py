# method 1
class Solution:
    def constructArray(self, n: 'int', k: 'int') -> 'List[int]':
        a = list(range(1,n+1))
        
        for i in range(1,k):
            a[i:] = a[:i-1:-1]
        return a

#method 2

        s = []
        head, tail = 1, n
        
        while head<=tail:
            if k>1:
                if k%2 == 1:
                    s.append(head)
                    head = head + 1
                else:
                    s.append(tail)
                    tail  = tail -1
                    
                k = k - 1
            else:
                s.append(head)
                head = head + 1
        return s

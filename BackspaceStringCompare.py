class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ans1 = []
        ans2 = []
        
        def typed(S):
            ans = []
            s = len(S)
            for i in range(s):
                if S[i] != '#':
                    ans.append(S[i])
                else:
                    ans and ans.pop()
            return ans
        
        ans1 = typed(S)
        ans2 = typed(T)
        
        return ans1 == ans2

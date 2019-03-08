class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1]*amount
        
        for i in range(amount):
            if dp[i] < 0:
                continue
            for coin in coins:
                if coin+i > amount:
                    continue  
                if (dp[coin+i] < 0) or (dp[coin+i] > dp[i] + 1):
                    dp[coin+i] = dp[i] + 1
        
        return dp[amount]

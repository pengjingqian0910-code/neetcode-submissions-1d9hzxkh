class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字串有一種解碼方式（不選）
        dp[1] = 1  # 第一個字元只要不是0就有1種解碼

        for i in range(2, n + 1):
            # 單個數字有效
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # 兩位數字有效
            two = int(s[i - 2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

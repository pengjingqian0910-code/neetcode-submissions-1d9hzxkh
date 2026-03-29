class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):          # i 從後往前
            for j in range(i, n):              # j 從 i 向右
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i+1][j-1]:   # 中間是回文，或長度 <= 2
                        dp[i][j] = True
                        count += 1
        return count

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 記錄每個字母出現次數
        max_count = 0  # 當前視窗內最常出現字母的次數
        l = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count[s[r]])

            # 如果要讓整段字串成為一樣的字元，超出了k次替換，就縮小視窗
            if (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result

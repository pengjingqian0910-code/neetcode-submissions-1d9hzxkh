class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []  # 用來存當前不重複子字串的字元
        max_length = 0

        for c in s:
            if c in seen:
                # 若遇到重複字元，從重複字元之後開始新的子字串
                idx = seen.index(c)
                seen = seen[idx+1:]
            seen.append(c)
            max_length = max(max_length, len(seen))

        return max_length

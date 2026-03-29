class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        repeat = set() 
        result,maxleng = 0,0
        for i,c in enumerate(s):
            while c in repeat:
                repeat.remove(s[left])
                left += 1
            right+=1
            repeat.add(c)
            result = right - left
            if result > maxleng:
                maxleng = result
        return maxleng
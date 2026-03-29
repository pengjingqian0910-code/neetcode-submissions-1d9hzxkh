class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        leng = len(temperatures)
        ans = [0] * leng
        for i in range (leng):
            while  stack and (temperatures[i]>temperatures[stack[-1]]):
                r = stack.pop()
                ans[r] = i-r
            stack.append(i)
        return ans
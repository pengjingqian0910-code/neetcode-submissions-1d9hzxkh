class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化三個變數
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        
        # 從第二個數字開始走
        for i in range(1, len(nums)):
            curr = nums[i]

            temp_max = max_so_far
            
            max_so_far = max( curr, temp_max*curr , curr*min_so_far)
            min_so_far = min( curr, min_so_far*curr , curr*temp_max)

            if (max_so_far > result):
                result = max_so_far
        return result

        
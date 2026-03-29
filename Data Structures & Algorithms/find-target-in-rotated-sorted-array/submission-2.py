class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # 第一步：先找出「最小值的位子」（就是你上一題學的！）
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l 
        if target >= nums[pivot] and target <= nums[len(nums)-1]:
            l, r = pivot, len(nums) - 1
        else:
            # 在左邊這段
            l, r = 0, pivot - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1 
            else:
                return mid
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,l,r = 0,0,len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                return -1
        return -1
        

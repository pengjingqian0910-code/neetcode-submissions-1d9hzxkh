import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. 虛擬速度的最小值與最大值
        low = 1
        high = max(piles)
        
        while low <= high:
            mid_k = (low + high) // 2 # 這就是我們猜的「虛擬速度」
            # 2. 用這個速度去測試，看要花幾小時
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid_k)
            
            # 3. 根據測試結果縮小範圍
            if total_time <= h:
                # 速度夠快，試試看能不能更慢一點
                high = mid_k - 1
            else:
                # 速度太慢，必須加快
                low = mid_k + 1
        
        # 最後 low 會停在「剛好能過關」的最小速度上
        return low
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Time: nlogn
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (l + r) // 2
            if self._can_deliver(weights, days, m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res


    def _can_deliver(self, weights: List[int], days: int, ship_cap: int) -> bool:
        # can deliver weights in `days` days with given capacity
        cnt = 1
        cap_used = 0

        for weight in weights:
            if cap_used + weight > ship_cap:
                cnt += 1
                cap_used = 0
            
            cap_used += weight


        return cnt <= days
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = r = 0
        
        while r < len(arr):
            if r - l < k:
                # we don't need to shrink window
                r += 1
                continue
            
            if is_closer(arr[l], arr[r], x):
                break
            
            l += 1
            r += 1


        return arr[l: r]


def is_closer(a, b, x):
    """is a closer to x than b"""
    if abs(a-x) < abs(b-x):
        return True
    elif abs(a-x) == abs(b-x) and a < b:
        return True
    
    return False
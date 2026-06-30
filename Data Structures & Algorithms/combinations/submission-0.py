class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # go for 1 to n, take 2 actions recursively:
        # Take or don't take current elemnt into the combination
        # if the combination is too long break and don't append
        # if the combination reached n and is too short also break
        # and don't append
        res = []

        def backtrack(x: int, arr: List[int]):
            if len(arr) == k:
                res.append(arr.copy())
                return

            if x > n:
                return
            
            # add x
            arr.append(x)
            backtrack(x + 1, arr)
            arr.pop()

            # skip x
            backtrack(x + 1, arr)
            
        backtrack(1, [])

        return res

            

            

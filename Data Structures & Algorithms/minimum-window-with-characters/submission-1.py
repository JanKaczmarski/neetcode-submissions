class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # try to achieve valid window
        # when valid try to shorten it but maintaing the valid seq all the time

        l = 0
        res = (float('inf'), -1, -1) # l and r of shortest valid substring
        want, have = {}, {}
        valid = False

        for ch in t:
            want[ch] = want.get(ch, 0) + 1

        for r in range(len(s)):
            have[s[r]] = have.get(s[r], 0) + 1
            valid = is_valid(want, have)

            while valid and l <= r:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                
                have[s[l]] -= 1
                l += 1
                valid = is_valid(want, have)

        _, start, end = res

        return s[start:end + 1]
            
            # we have valid subseq

def is_valid(want, have):
    for key, value in want.items():
        if key not in have or have[key] < value:
           return False

    return True

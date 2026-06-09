class Solution:
    def minWindow(self, s: str, t: str) -> str:
        want = {}
        for ch in t:
            want[ch] = want.get(ch, 0) + 1

        have = {}
        formed = 0
        required = len(want)

        l = 0
        res_len = float("inf")
        res_l = 0
        res_r = 0

        for r in range(len(s)):
            ch = s[r]
            have[ch] = have.get(ch, 0) + 1

            if ch in want and have[ch] == want[ch]:
                formed += 1

            while formed == required:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_l = l
                    res_r = r

                left_ch = s[l]
                have[left_ch] -= 1

                if left_ch in want and have[left_ch] < want[left_ch]:
                    formed -= 1

                l += 1

        if res_len == float("inf"):
            return ""

        return s[res_l : res_r + 1]

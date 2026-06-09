class Solution:
    def validPalindrome(self, s: str) -> bool:
        def rek(s:str, removed: bool):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                    continue
                if removed:
                    return False
                
                # remove left
                if rek(s[l + 1: r + 1], True):
                    return True
                # remove right
                elif rek(s[l: r], True):
                    return True

                return False

            return True
                
        return rek(s, False)
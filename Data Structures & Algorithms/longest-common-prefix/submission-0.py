class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "" 

        res = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return res
            common = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != common:
                    return res

            res += common
            i += 1

        return res
                


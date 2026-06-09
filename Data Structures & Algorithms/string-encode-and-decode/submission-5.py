DELIMIT = "#"

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + DELIMIT + s
        
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0

        while i < len(s):
            jump_str = ""
            while i < len(s) and s[i] != DELIMIT:
                jump_str += s[i]
                i += 1

            # 3#asd

            jump = int(jump_str)
            res.append(s[i+1 : i + jump+1])
            i += jump + 1

        return res

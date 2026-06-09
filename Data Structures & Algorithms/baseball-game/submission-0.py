class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # push values to stack so we can store the results 
        # and access the previous element
        s = []

        for i, op in enumerate(operations):
            if op == "+":
                prev = s.pop()
                prev_prev = s.pop()
                
                s.append(prev_prev)
                s.append(prev)

                s.append(prev + prev_prev)
            elif op == "D":
                s.append(s[-1] * 2)
            elif op == "C":
                s.pop()
            else:
                val = int(op)
                s.append(val)
        
        res = 0
        while s:
            res += s.pop()

        return res
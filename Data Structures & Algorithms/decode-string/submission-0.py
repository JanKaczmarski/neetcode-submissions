class Solution:
    def decodeString(self, s: str) -> str:
        # if [ is met add the current string to stack
        # if ] is met the current element is done and we can return it upward
        # we now combine with upward (we have to keep in mind the multiplier)

        # input, multiplier_cur, cur, stack
        # 2[a3[b]]c, -1, "", []
        # 2, "a", []
        # 3, "b", [(2, "a")]
        # 2, "abbb", [] ] close bracket - append current mul with cur to the element in the stack - if stack non-empty

        stack = []
        cur_mul, cur = -1, ""
        
        i = 0
        while i < len(s):
            if not s[i].isdigit() and s[i] != "]":
                cur += s[i]
            elif s[i].isdigit(): # first digit met - load the multiplier
                stack.append((cur_mul, cur)) # store current seq

                new_mul_str = ""
                while s[i].isdigit():
                    new_mul_str += s[i]
                    i += 1
                
                cur_mul = int(new_mul_str)
                cur = ""

            else: # == "]"
                # add current to top of the stack - cannot be empty
                old_mul, old_cur = stack.pop()

                old_cur += int(cur_mul) * cur

                cur_mul = old_mul
                cur = old_cur

            i += 1

        return cur



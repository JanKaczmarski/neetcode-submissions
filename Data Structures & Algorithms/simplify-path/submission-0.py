class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # skip consecutive `/`
        # .. removes last directory from stack - if any directory on stack
        # search for elements between slashes -> split on `/` and skip empty elemnts (multiples slahses)

        path_spl = path.split("/")

        for elem in path_spl:
            # skip (multiple slash or cur dir)
            match elem:
                case "" | ".":
                    continue
                case "..":
                    if stack: stack.pop()
                case _: # dir name
                    stack.append(elem)

        #print(stack)

        return "/" + "/".join(stack)

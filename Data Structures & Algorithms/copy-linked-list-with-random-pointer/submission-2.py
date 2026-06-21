"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # random can be computed by offset from current node - so assign each node a value idx
        # bind random to idx, next deepcopy a linked list and have indexes at each element assign mem addr
        # random to where the idx should point to

        # [3,null],[7,3],[4,0],[5,1]

        # [3,null, 0],[7,3, 1],[4,0, 2],[5,1, 3]

        # deepcopy without `random` and store idx-memAddr in map
        # [3, null], [7, null], [4, null], [5, null] | [0, addr(3)], [1, addr(7)], ...

        # go through the original linked list and based on indexes assign random in depe copy

        # Time: O(n) - size of input linked list
        # Space: O(n)

        

        # create a map of [original : copy] the key adn value will be the object itself
        # random can be recreated from this mapping

        store = {}
        head_iter = head


        while head_iter:
            new_node = Node(head_iter.val)
            store[head_iter] = new_node

            head_iter = head_iter.next

        head_iter = head
        while head_iter:
            cp_node = store[head_iter]

            if head_iter.next:
                cp_node.next = store[head_iter.next]
            if head_iter.random:
                cp_node.random = store[head_iter.random]
            else:
                cp_node.random = None

            head_iter = head_iter.next

        if head:
            return store[head]

        return None


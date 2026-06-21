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

        # 1. assign idx to original nodes
        orig_idx = {} # node : idx
        cp_idx = {} # idx : node
 
        d_head = Node(0)
        
        iter_d_head = d_head
        iter_head = head
        idx = 0
        while iter_head:
            new_node = Node(iter_head.val)
            iter_d_head.next = new_node

            orig_idx[iter_head] = idx
            cp_idx[idx] = new_node

            idx += 1
            iter_d_head = iter_d_head.next
            iter_head = iter_head.next

        # reset iter head
        iter_head = head

        while iter_head:
            random_node = iter_head.random
            if random_node != None:
                random_node_idx = orig_idx[random_node]
                iter_head_idx = orig_idx[iter_head]

                cp_idx[iter_head_idx].random = cp_idx[random_node_idx]

            iter_head = iter_head.next        


        return d_head.next # skip guard
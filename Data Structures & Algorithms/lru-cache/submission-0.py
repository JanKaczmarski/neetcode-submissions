from typing import Dict, Optional


class Node:
    def __init__(self, x: int = 0, key: int = 0, nxt: "Node" = None, prev: "Node" = None):
        self.x = x
        self.key = key
        self.nxt = nxt
        self.prev = prev



class LRUCache:
    def __init__(self, capacity: int):
        self.head = None  # most recently used
        self.tail = None  # least recently used
        self.size = 0
        self.capacity = capacity
        self.store: Dict[int, Optional[Node]] = {}

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        nd = self.store[key]

        if nd != self.head:
            # detach nd
            if nd.prev:
                nd.prev.nxt = nd.nxt
            if nd.nxt:
                nd.nxt.prev = nd.prev

            if nd == self.tail:
                self.tail = nd.nxt

            # move nd to head
            old_head = self.head
            nd.prev = old_head
            nd.nxt = None

            if old_head:
                old_head.nxt = nd

            self.head = nd

        return nd.x

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].x = value
            # update referesh LRU queue
            self.get(key)
            return

        if self.size == self.capacity:
            old_tail = self.tail

            # remove old tail from store
            del self.store[old_tail.key]

            if self.capacity == 1:
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.nxt
                self.tail.prev = None

            self.size -= 1

        nd = Node(value, key, None, self.head)
        self.store[key] = nd
        self.size += 1

        if self.head:
            self.head.nxt = nd

        self.head = nd

        if self.size == 1:
            self.tail = nd
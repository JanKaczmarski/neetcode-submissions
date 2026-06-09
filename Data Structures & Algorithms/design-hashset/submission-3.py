from typing import Dict, List

class MyHashSet:

    def __init__(self):
        self.hash_size = 10000
        self.store: List[List[int]] = [[] for _ in range(self.hash_size)]

    def add(self, key: int) -> None:
        hashed_val = self._hash_func(key)
        if key not in self.store[hashed_val]:
            self.store[hashed_val].append(key)

    def remove(self, key: int) -> None:
        hashed_val = self._hash_func(key)
        
        try:
            self.store[hashed_val].remove(key)
        except ValueError:
            # if key not in set we're fine
            pass

    def contains(self, key: int) -> bool:
        hashed_val = self._hash_func(key)
        return key in self.store[hashed_val]

    def _hash_func(self, key: int) -> int:
        # values are from range 0 to 1,000,000
        return key % self.hash_size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
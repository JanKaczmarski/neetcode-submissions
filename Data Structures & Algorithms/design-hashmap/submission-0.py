from typing import List, Tuple

class MyHashMap:

    def __init__(self):
        self._hash_size = 10000
        self.mymap: List[List[Tuple[int, int]]] = [[] for _ in range(self._hash_size)]
        

    def put(self, key: int, value: int) -> None:
        hashed_key = self._hash_func(key)
        found_idx = -1
        for i, (stored_key, _) in enumerate(self.mymap[hashed_key]):
            if stored_key == key:
                found_idx = i
                break
        
        if found_idx == -1:
            self.mymap[hashed_key].append((key, value))
        else:
            self.mymap[hashed_key][found_idx] = (key, value)
        

    def get(self, key: int) -> int:
        hashed_key = self._hash_func(key)
        for stored_key, value in self.mymap[hashed_key]:
            if stored_key == key:
                return value

        return -1
        

    def remove(self, key: int) -> None:
        hashed_key = self._hash_func(key)
        found_idx = -1
        for i, (stored_key, _) in enumerate(self.mymap[hashed_key]):
            if stored_key == key:
                found_idx = i
                break

        if found_idx == -1:
            return

        self.mymap[hashed_key].pop(found_idx)
        
    def _hash_func(self, key: int) -> int:
        return key % self._hash_size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
class MyCircularQueue:

    def __init__(self, k: int):
        # Use array of len k and 2 poitners - head and tail
        # if the head == tail and enqueue - we replcae head
        # if the head != tail we insert a new elment at tail
        self.buffer = [-1] * k
        self.capacity = k
        # easier is to start in the middle, but that doens't work for k == 1
        self.read = 0
        self.write = 0
        self.size = 0

        # write:
        # - write == read -> enqueue and write++ and read++
        # - write != read -> enqueue and write++

        # dequeue:
        # - size == 0: False
        # - size > 0: read++
        
        # front:
        # - size > 0: buffer[read]
        
        # rear:
        # - size > 0: buffer[write]


    def enQueue(self, value: int) -> bool:
        if self.size == 0: # emtpy queue - edge case
            self.buffer[self.write] = value
            self.read = self.write

            self.write = (self.write + 1) % self.capacity
            self.size += 1
            return True
        
        if self.write == self.read: # full queue
            #self.buffer[self.write] = value
            #self.write = (self.write + 1) % self.capacity
            #self.read = (self.write + 1) % self.capacity
            return False
        
        self.buffer[self.write] = value
        self.write = (self.write + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.read = (self.read + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size > 0:
            return self.buffer[self.read]
        return -1

    def Rear(self) -> int:
        if self.size > 0:
            rear_idx = (self.write - 1) % self.capacity
            return self.buffer[rear_idx]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class CircularLossBuffer:
    def __init__(self, capacity: int):
        self.buffer = [None]*capacity
        self.capacity =  capacity

        self.write_index = 0
        self.current_size = 0
    def push(self, loss: float):
        if self.current_size == self.capacity:
            self.buffer[self.write_index] = loss 
            self.write_index = (self.write_index + 1) % self.capacity
        else:
            self.buffer[self.write_index] = loss
            self.write_index = (self.write_index + 1) % self.capacity 
            self.current_size = self.current_size + 1
    def mean(self) -> float:
        if self.current_size == 0:
            return 0.0
        
        total_loss = 0.0
        for item in self.to_list():
            total_loss += item
        return total_loss / self.current_size
    def to_list(self) -> list:
        if self.current_size == self.capacity:
            return self.buffer[self.write_index:] + self.buffer[:self.write_index]
        else:
            return self.buffer[:self.current_size]
    def is_converged(self, threshold: float) -> bool:
        lst = self.to_list()
        maximum = lst[0]
        for num in lst:
            if num > maximum:
                maximum = num
        minimum = lst[0]
        for num in lst:
            if num < minimum:
                minimum = num
        if (maximum - minimum) < threshold:
            return True
        else:
            return False
buf = CircularLossBuffer(capacity=5)
for loss in [2.1, 1.9, 1.7, 1.5, 1.3, 1.1, 0.9]:
    buf.push(loss)
    print(buf.to_list(), 'mean:', buf.mean())
CircularLossBuffer(0).push(1.0)
        
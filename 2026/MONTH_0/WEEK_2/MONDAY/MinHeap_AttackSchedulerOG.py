class MinHeap:
    def __init__(self):
        self.tree = []
    def push(self, priority: float , item: str):
        self.tree.append((priority,item))
        self._sift_up()
    def _sift_up(self): 
        i = len(self.tree) - 1
        j = (i-1) // 2
        while i != 0 and self.tree and self.tree[i] < self.tree[j]:
            self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
            i = j
            j = (i - 1) // 2
    def pop(self):
        i = len(self.tree) - 1    
        root = self.tree[0]
        self.tree[0] = self.tree[i]
        self.tree.pop(i)
        self._sift_down()
        return root
    def _sift_down(self):
        i = 0
        j = (2*i) + 1
        while j < len(self.tree):
            k = (2*i) + 2
            if self.tree[i] > self.tree[j]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                i = j
            elif k < len(self.tree) and self.tree[i] > self.tree[k]:
                self.tree[i], self.tree[k] = self.tree[k], self.tree[i]
                i = k
            else:
                break
    def is_empty(self):
        if len(self.tree) == 0:
            return True
        if len(self.tree) != 0:
            return False
    def peek(self):
        return self.tree[0]
    def size(self):
        return len(self.tree)
class AttackScheduler:
    def __init__(self):
        self.heap = MinHeap()
    def schedule(self, attack_name: str, priority:float):
        self.heap.push(priority,attack_name)
    def next_attack(self) -> tuple:
        return self.heap.pop()
    def pending(self):
        return len(self.heap.tree)
sched = AttackScheduler()
sched.schedule('FGSM_batch_01', priority=0.03)
sched.schedule('PGD_batch_01', priority=0.001)
sched.schedule('CW_batch_01', priority=0.5)
sched.schedule('GCG_token_01', priority=0.0001)

while not sched.heap.is_empty():
    print(sched.next_attack())

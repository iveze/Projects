class BinaryHeap:
    def __init__(self, data = None):
        if data is not None:
            self.build_heap(data)
        else:
            self.heap = []
            self._length = 0

    def add(self, value) -> None:
        self._length += 1
        self.heap.append(value)
        i = self._length - 1
        parent = int((i - 1) / 2)
        while i > 0 and self.heap[parent] < self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = int((i - 1) / 2)


    def heapify(self, i) -> None:
        left = i * 2 + 1
        right = i * 2 + 2

        if left < self._length and self.heap[left] > self.heap[i]:
            self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
            self.heapify(left)
        
        if right < self._length and self.heap[right] > self.heap[i]:
            self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
            self.heapify(right)


    def build_heap(self, data) -> None:
        self.heap = data
        self._length = len(data)
        for i in range(int(self._length / 2), -1, -1):
            self.heapify(i)

    def get_max(self) -> int:
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.remove(self.heap[-1])
        self._length -=1 
        self.heapify(0)
        return result
    
    def sort(self):
        for i in range(self._length):
            self.get_max()



myheap = BinaryHeap([1, 10, 11, 12, 1000, 2, 3, 4, 6, 9])
ll = [1, 10, 11, 12, 1000, 2, 3, 4, 6, 9]
#for el in ll:
#    myheap.add(el)
print(myheap.heap)
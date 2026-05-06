class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.num = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.num == self.capacity:
            self.resize()
        self.arr[self.num] = n
        self.num+=1

    def popback(self) -> int:
        if self.num > 0:
            self.num-=1
        return self.arr[self.num]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newArray = [0] * self.capacity
        
        for i, val in enumerate(self.arr):
            newArray[i] = val
        self.arr = newArray

    def getSize(self) -> int:
        return self.num
    
    def getCapacity(self) -> int:
        return self.capacity

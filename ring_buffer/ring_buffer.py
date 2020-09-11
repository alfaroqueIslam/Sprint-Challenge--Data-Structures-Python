class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None for i in range(capacity)]
        self.old = self.data[0]
        self.old1 = None
  
    def append(self, item):
        lst = []
        if self.data[0] == None:
            self.data.pop(0)
            self.data.append(item)
            if self.data[0] != None:
                self.old = self.data[0]
            return
        for n in self.data:
            if n != None:
                lst.append(n)
        if len(lst) == self.capacity:
            if self.data[0] == self.old:
                self.data[0] = item
                self.old1 = item
                return
            else:
                x = lst.index(self.old1)
                self.data[x+1] = item
                self.old = item

    def get(self):
        lst = []
        for n in self.data:
            if n != None:
                lst.append(n)

        return lst
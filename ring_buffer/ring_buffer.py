class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None for i in range(capacity)]
        self.old = self.data[0]
        self.x = 0
  
    def append(self, item):
        if self.data[0] == None:
            self.data.pop(0)
            self.data.append(item)
            if self.data[0] != None:
                self.old = self.data[0]
            return

        if self.data[0] == self.old and self.x == 0:
            self.data[0] = item
            self.old = item
            self.x = 1
            return
        else:
            x = self.data.index(self.old)
            if x == self.data.index(self.data[-1]):
                self.old = self.data[0]
                self.data[0] = item
                self.old = self.data[0]
                return
            self.data[x+1] = item
            self.old = item
            return

    def get(self):
        lst = []
        if self.data[0] == None:
            for n in self.data:
                if n != None:
                    lst.append(n)

            return lst
        return self.data
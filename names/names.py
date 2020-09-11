import time
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return
                #return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return self.value

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value),
        if self.right:
            self.right.for_each(fn)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# duplicates = set(names_1).intersection(names_2)

bn = BSTNode(names_2[0])

for i in names_2[1:]:
    bn.insert(i)

for s in names_1:
   if bn.contains(s) == s:
       duplicates.append(s)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

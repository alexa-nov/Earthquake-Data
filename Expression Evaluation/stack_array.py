class StackArray:
    def __init__(self):
        self.arr = [None] * 2
        self.capacity = 2
        self.num_items = 0
        
    def __eq__(self, other):
        return isinstance(other, type(self))\
               and self.arr == other.arr\
               and self.capacity == other.capacity\
               and self.num_items == other.num_items
    def __repr__(self):
        return "Stack Array {Array: (%s), Capacity: (%d), Num Items: (%d)}"\
               %(self.arr, self.capacity, self.num_items)


    def enlarge(self):
        """ Creates a new array with double capacity
        Attributes:
          Nothing
        Returns:
          list: a larger new array
        """
        to_copy = self.arr
        new_arr = [None] * self.capacity * 2 
        for i in range(self.num_items):
            new_arr[i] = to_copy[i]
        self.arr = new_arr
        self.capacity = self.capacity * 2
        return self.arr

    def shrink(self):
        """ Creates a new array with smaller capacity
        Attributes:
          Nothing
        Returns:
          list: a smaller new array
        """
        to_copy = self.arr
        new_arr = [None] * (self.capacity // 2)
        for i in range(self.num_items):
            new_arr[i] = to_copy[i]
        self.arr = new_arr
        self.capacity = self.capacity //  2
        return self.arr

    def pop(self):
        """ Removes item from the top of the stack
        Attributes:
          Nothing
        Returns:
          int: item removed
        """
        if self.num_items == 0:
            raise IndexError
        elif self.capacity / self.num_items >= 4:
            self.shrink()
            item_removed = self.arr[self.num_items - 1]
            self.arr[self.num_items - 1] = None
            self.num_items -= 1
            return item_removed
        else:
            item_removed = self.arr[self.num_items - 1]
            self.arr[self.num_items - 1] = None
            self.num_items -= 1
            return item_removed

    def push(self,item):
        """ Adds a new item to the top of the stack
        Attributes:
          item (int): item to add to stack
        Returns:
         Nothing
        """
        if self.capacity == self.num_items:
            self.enlarge()
            self.arr[self.num_items] = item
            self.num_items += 1
            return
        else:
            self.arr[self.num_items] = item
            self.num_items += 1
            return
       

    def peek(self):
        """ Returns top item from the stack
        Attributes:
          Nothing
        Returns:
          int: item at top of stack
        """
        if self.num_items == 0:
            raise IndexError
        return self.arr[self.num_items - 1]

    def is_empty(self):
        """ Checks if stack is empty
        Attributes:
          Nothing
        Returns:
          boolean: True if empty, False is not empty
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """ Returns number of items in stack
        Attributes:
          Nothing
        Returns:
          int: size of stack
        """
        return self.num_items

class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0                              #Count is how much is currently used
        self.capacity = capacity                    #How much total space is currently allocated wether we are using it or not
        self.storage = [None] * self.capacity       #self.storage is our pointer?

    def insert(self, index, value):                 #checking if there is any room to add
        if self.count == self.capacity:
            self.resize()
            return
        
        #Shift everything to the right 1 space
                        #starting, stopping
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        #Insert our value and increase the count of how much memory is being used by 1:
        self.storage[index] = value
        self.count += 1

    def append(self, value):                      #appending the new value
        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        #changing the pointer 
        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value  #O(1)

    def add_to_front(self, value):
        self.insert(0, value)

    def slice(self, begining_index, end_index): # default value
        # beggining and end
        # create subarray to store values

        # copy beginning to end to subarray

        # decide how this works. What happens to the original array?
            # Leave it alone? Or cut out what we're slicing?

        # return subarray
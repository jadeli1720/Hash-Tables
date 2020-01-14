# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key          # array index for a hash table
        self.value = value
        self.next = None        # next is the pointer

    def __repr__(self):
        return f"Key = {self.key}, Value = {self.value}"
    

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity      # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __repr__(self):
        return f"Storage = {self.storage}"


    def _hash(self, key): #done
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key): #stretch
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):#done
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

# do the below functions: --> use linked list operations. Similar (data-structures material)
    def insert(self, key, value): 
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # traverse down the linked list to see if the key is already there
        index = self._hash_mod(key)
        # print("Index", index)
        current_pair = self.storage[index] # node 
        # print("Current Pair", current_pair.key) # prints to none --> pointer helps us to move through list
        last_pair = None #pointer

        while current_pair is not None and current_pair.key is not key :
            # print("while statement")
            last_pair = current_pair
            current_pair = last_pair.next

        if current_pair is not None:
            # if the key does exist, than you want to overwrite the value
            # print("Hitting top of if statement", current_pair.value)
            current_pair.value = value
            
        else: # if we hit none or null, then we know it's not there
            # add to the end of the link list (creating a new value)
            newLinkedPair = LinkedPair(key,value)
            newLinkedPair.next = self.storage[index]
            self.storage[index] = newLinkedPair 
            print("In else statement",self.storage[index])

        
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # print("Retrieve index",index)
        current_key = self.storage[index]
        while current_key:
            if current_key.key != key:
                current_key = current_key.next
                # print("Current Key",current_key)
            else:
                return current_key.value
        return None    

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


# myHt = HashTable(2)

# # print(myHt)

# myHt.insert("grapes", 12)
# print(myHt)
#     # print("ht", ht)
# print('Retirieve',myHt.retrieve('grapes'))

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # Test storing beyond capacity
    print('Retrieve line 1',ht.retrieve("line_1"))
    print('Retrieve line 2',ht.retrieve("line_2"))
    print('Retrieve line 3',ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")

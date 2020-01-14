# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key          # array index for a hash table
        self.value = value
        self.next = None        # next is the pointer

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity      # Number of buckets in the hash table
        self.storage = [None] * capacity


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
        current_value = self.storage[index]
        # print("Current Value", current_value) # prints to none --> pointer helps us to move through list

        if current_value is not None:
            # if the key does exist, than you want to overwrite the value
            print("Warning", value, "is overwriting", current_value.value)
            newLinkedPair = LinkedPair(key, value)
            newLinkedPair.next = current_value
            current_value = newLinkedPair 
            
        else: # if we hit none or null, then we know it's not there
            # add to the end of the link list (creating a new value)
            current_value = LinkedPair(key, value)
        
        
        
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
        current_key = self.storage[index]
        while current_key:
            if current_key.key != key:
                current_key = current_key.next
                print("Current Key",current_key)
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



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

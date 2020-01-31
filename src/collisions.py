import random
import statistics


def how_many_before_collisions(buckets, loops=1):
    """
    Roll random hashes into 'buckets' (capacity) and print
    how many rolls before a hash collision.

    Run 'loops' number of times
    """

    for i in range(loops):
        tries = 0
        tried = set()      #using set because we don't care what the keys are
        
        results = []

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets

            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break   # we have a collision so break

        result = tries / buckets * 100
        results.append(result)
        
        print(f"\nBuckets: {buckets}\nHashes Before Collision: {tries} ({tries / buckets * 100:.1f}%)\n") # --> cleaner print statement
        # print(f"\nBuckets: {buckets}\nHashes Before Collision: {tries} ({result:.1f}%)\n") # --> cleaner print statement
    
    # print(statistics.mean(results))
    # print(f"Results: {results}\n") # --> cleaner print statement
    print(f"Average of 'Results' Array: {statistics.mean(results)} hashes before collision\n") # --> cleaner print statement
    


how_many_before_collisions(32, 10)
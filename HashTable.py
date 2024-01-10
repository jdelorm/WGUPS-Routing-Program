# Class for Hash Table

class HashTable:

    # Method that initializes the hash table
    def __init__(self, initial_capacity=40):
        self.table = [[] for _ in range(initial_capacity)]

    # Method that inserts data into the hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key in bucket_list:
            if key[0] == key:
                key[1] = item
                return True

        bucket_list.append([key, item])
        return True

    # Method that searches the hash table using a key
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]

        return None

    # Method that deletes data from the hash table using a key
    def delete(self, key):
        slot = hash(key) % len(self.table)
        destination = self.table[slot]

        if key in destination:
            destination.remove(key)

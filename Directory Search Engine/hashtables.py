from node import Node


class HashTableSepchain:
    """ Hashtable with Separate Chaining
    Attributes:
        table_size (int): size of table
        hash (list): hash table
        num_items (int): number of items
        num_collisions (int): number of collisions
    """

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash = [None] * table_size
        self.num_items = 0
        self.num_collisions = 0

    def __eq__(self, other):
        return isinstance(other, type(self)) \
               and self.table_size == other.table_size \
               and self.hash == other.hash \
               and self.num_items == other.num_items \
               and self.num_collisions == other.num_collisions

    def __repr__(self):
        return "Sepchain: (%s), Table Size: (%d), Num Items: (%d), Num Collisions: (%d)" \
               % (self.hash, self.table_size, self.num_items, self.num_collisions)

    # gets a value with []
    def __getitem__(self, key):
        return self.get(key)

    # enables value assignment with []
    def __setitem__(self, key, data):
        self.put(key, data)

    # Enables in operator on hash table
    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """ Inserts key-value pair into hash table
        Arguments:
            key (str): key to be inserted into hash table
            data (any): data associated with key
        """
        self.num_items += 1
        if self.load_factor() >= 1.5:
            new_table_size = 2 * self.table_size + 1
            self.table_size = new_table_size
            self.resize()
        val = hash_string(key, self.table_size)
        node_to_push = Node(key, data)
        if self.hash[val] is None:
            self.hash[val] = node_to_push
            return
        if self.hash[val] is not None:
            old_top = self.hash[val]
            node_to_push.next = old_top
            self.hash[val] = node_to_push
            return
        self.num_collisions += 1

    def get(self, key):
        """ Returns the value from a key-value pair
        Arguments:
            key (str): key to be found
        Returns:
            any: value associated with key found
        Raises:
            KeyError: if key-val does not exist
        """
        val_hash = hash_string(key, self.table_size)
        if self.hash[val_hash].key == key:
            return self.hash[val_hash].val
        if self.hash[val_hash].key != key:
            loop_val = self.hash[val_hash]
            while loop_val.next is not None:
                if loop_val.next.key == key:
                    return loop_val.next.val
                loop_val = loop_val.next
        raise KeyError()

    def keys(self):
        """ Returns a list of keys in the hash table
        Returns:
            list: keys in hash table
        """
        list_keys = []
        for node in self.hash:
            while node is not None:
                list_keys.append(node.key)
                node = node.next
        return list_keys

    def contains(self, key):
        """ Checks to see if a key exists
        Arguments:
            key (str): key to be search for
        Returns:
            boolean: True if found, False if not
        """
        try:
            self.get(key)
            return True
        except:
            return False

    def remove(self, key):
        """ Removes a key-value pair from the hash table
        Arguments:
            key (str): key to be removed from hash table
        Returns:
            Node: key-value pair removed
        Raises:
            KeyError: if key-val does not exist
        """
        if not self.contains(key):
            raise KeyError
        idx = hash_string(key, self.table_size)
        item = self.hash[idx]
        if self.hash[idx].key == key:
            temp = self.hash[idx]
            self.hash[idx] = self.hash[idx].next
            self.num_items -= 1
            return temp
        while item is not None and item.next.key != key:
            item = item.next
        temp = item.next
        item.next = item.next.next
        self.num_items -= 1
        return temp

    def size(self):
        """ Returns size of hash table
        Returns:
            int: num items in hash table
        """
        return self.num_items

    def load_factor(self):
        """ Returns load factor of hash table
        Returns:
            int: current load factor of hash table
        """
        return self.num_items / self.table_size

    def collisions(self):
        """ Returns number of collisions that have occurred during insertion
        Returns:
            int: number of collisions
        """
        return self.num_collisions

    def resize(self):
        """ Resizes the hash table
        """
        self.num_collisions = 0
        temp_num_items = self.num_items
        temp = self.hash
        self.hash = [None] * self.table_size
        for item in temp:
            if item is not None:
                node = item
                while node is not None:
                    self.put(node.key, node.val)
                    node = node.next
        self.num_items = temp_num_items


def hash_string(string, size):
    """ Hash function for string key
    Arguments:
        string (str): str key
        size (int): size of hash table
    Returns:
        int: hash value
    """
    hash_val = 0
    for char in string:
        hash_val = (hash_val * 31 + ord(char)) % size
    return hash_val


def import_stopwords(filename, hashtable):
    """
    Arguments:
        filename (str): name of file
        hashtable (HashTable): object of HashTable classes
    Return:
        HashTable: a HashTable object
    """
    file = open(filename, "r")
    words = [line for line in file]
    words = ''.join(words)
    words = words.split()
    for word in words:
        hashtable.put(word, 0)
    file.close()
    return hashtable

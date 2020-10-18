class Node:
    """A Linked List is one of
      - None, or
      - Node(val,next): A Linked List
    Attributes:
      key (str): a key for the val
      val (any): the payload of any type
      next (Node): a Linked List
    """
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

    def __eq__(self, other):
        return isinstance(other, type(self)) \
               and self.key == other.key \
               and self.val == other.val \
               and self.next == other.next

    def __repr__(self):
        return "Node: (Key: {}, Val: {}, Next: {})".format(self.key, self.val, self.next)

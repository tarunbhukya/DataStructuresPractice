"""
   CircularQueue of a fixed size
"""


class CircularQueue:
    """
        Args:
            kth_size: CircularQueue Size
    """

    def __init__(self, kth_size):
        self.kth_size = kth_size
        self.head_pointer = -1
        self.tail_pointer = -1
        self.array_list = [None] * self.kth_size

    def enqueue(self, x):
        if self.is_full():
            return False
        if self.is_empty():
            self.head_pointer = 0

        self.tail_pointer = (self.tail_pointer + 1) % self.kth_size
        self.array_list[self.tail_pointer] = x
        return True

    def dequeue(self):
        if self.is_empty():
            return False

        if self.head_pointer == self.tail_pointer:
            self.head_pointer = -1
            self.tail_pointer = -1
            return True

        self.head_pointer = (self.head_pointer + 1) % self.kth_size
        return True

    def get_front(self):
        return self.array_list.__getitem__(self.head_pointer)

    def get_rear(self):
        return self.array_list.__getitem__(self.tail_pointer)

    def is_empty(self):
        return self.head_pointer == -1

    def is_full(self):
        return (self.tail_pointer + 1) % self.kth_size == self.kth_size

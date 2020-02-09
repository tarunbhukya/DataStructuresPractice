class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window_size = size
        self.current_window_size = 0
        self.sum = 0
        self.array_list = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if (self.current_window_size < self.window_size):
            self.array_list.append(val)
            self.sum += val
            self.current_window_size += 1
            return float(self.sum / self.current_window_size)
        else:
            delete_num = self.array_list.pop(0)
            self.array_list.append(val)
            self.sum = self.sum + val - delete_num
            return float(self.sum / self.window_size)

a = MovingAverage(3)
print (a.next(1))
print (a.next(10))
print (a.next(3))
print (a.next(5))
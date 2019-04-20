import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []


    def push(self, item, prioriry):
        heapq.heappush(self._queue, (-prioriry, item))


    def pop(self):
        return heapq.heappop(self._queue)[-1]



class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


a = (1, Item('foo'))
b = (5, Item('bar'))
c = (1, Item('gorl'))

print(a < b)
print(a < c)










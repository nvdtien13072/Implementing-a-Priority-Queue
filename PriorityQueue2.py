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


p = PriorityQueue()

p.push(Item('foor'),1)
p.push(Item('bar'),5)
p.push(Item('spam'),4)
p.push(Item('grok'),2)

a = (1, Item('foo'))
b = (5, Item('bar'))
c = (1, Item('gorl'))
a < b
a < c
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())










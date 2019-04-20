import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, prioriry):
        heapq.heappush(self._queue, (-prioriry,self._index, item))
        self._index += 1

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
p.push(Item('grok'),1)

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))

print (a > b)

print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())

# Kết quả của việc thực hiện đoạn code trên
# Item('bar')
# Item('spam')
# Item('grok')
# Item('foor')









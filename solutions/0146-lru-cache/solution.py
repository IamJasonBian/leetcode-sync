from collections import deque

class LRUCache:

    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.hashmap = {}
        self.deque = deque()

    def get(self, key: 'int'):
        res = self.hashmap.get(key, [-1, 0])[0]
        if res != -1:
            self.put(key, res)
        return res

    def put(self, key: 'int', value: 'int') -> 'None':

        self.add(key, value)
        while len(self.hashmap) > self.capacity:
            self.remove()

    def add(self, key, value):
        if key in self.hashmap:
            self.hashmap[key][1] += 1
            self.hashmap[key][0] = value
        else:
            self.hashmap[key] = [value, 1]
        self.deque.append(key)

    def remove(self):
        k = self.deque.popleft()
        self.hashmap[k][1] -=1
        if self.hashmap[k][1] == 0:
            del self.hashmap[k]
            

        


# Your LRUCache object will be instantiated and called as such:

#lRUCache.put(1, 1), key here is 1, value here is 1

# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]] (Case of 1 being removed by [4,1] due to capacity)



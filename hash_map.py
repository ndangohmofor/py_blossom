from linkedList import LinkedList
from node import Node



class HashMap:
    def __init__(self, size=0):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        hash_code = self.hash(key)
        array_index = self.compressor(hash_code)
        payload = Node([key, value])
        ll_at_index=self.array[array_index]
        for i in ll_at_index:
            if key == i[0]:
                i[1]=value
        ll_at_index.insert(payload)

    def retrieve(self, key):
        hash_code = self.hash(key)
        array_index = self.compressor(hash_code)
        payload = self.array[array_index]
        for i in payload:
            if key == i[0]:
                return i[1]
            else:
                return None
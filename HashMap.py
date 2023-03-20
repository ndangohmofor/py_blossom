class HashMap:
    def __init__(self, size=0):
        self.array_size = size
        self.array = [None for i in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        hash_code = self.hash(key)
        array_index = self.compressor(hash_code)
        self.array[array_index] = [key, value]

    def retrieve(self, key):
        hash_code = self.hash(key)
        array_index = self.compressor(hash_code)
        payload = self.array[array_index]
        if payload is not None:
            if payload[0] == key:
                return payload[1]
        else:
            return None
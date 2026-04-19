import math

class BloomFilter:
    def __init__(self, n, false_positive_rate):
        self.n = n
        self.p = false_positive_rate

        self.size = int(-n * math.log(self.p) / (math.log(2) ** 2))
        self.hash_count = int((self.size / self.n) * math.log(2))
        self.bit_array = bytearray(self.size // 8 + 1)

    def fnv_hash(self, word):
        hash_value = 2166136261
        for char in word:
            hash_value = (hash_value * 16777619) % (2 ** 32)
            hash_value = hash_value ^ ord(char)
        return hash_value
    
    def hashes(self, word):
        h1 = self.fnv_hash(word)
        h2 = self.fnv_hash(word + "#")

        for i in range(self.hash_count):
            yield (h1 + i * h2) % self.size

    def add(self, word):
        for index in self.hashes(word):
            print(index)
            self.bit_array[index // 8] |= (1 << (index % 8))

    def check(self, word):
        for index in self.hashes(word):
            if not (self.bit_array[index // 8] & (1 << (index % 8))):
                return False
        return True
    
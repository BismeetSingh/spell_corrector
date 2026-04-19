import string
import pickle
from src.bloom_filter.bloom_filter import BloomFilter

def generate_words_after_deleting_one_char(word):
    words = []
    for i in range(len(word)):
        words.append(word[:i] + word[i+1:])
    return words

def generate_words_after_inserting_one_char(word):
    words = []
    for i in range(len(word)):
        for char in string.ascii_lowercase:
            words.append(word[:i] + char + word[i:])
    return words

def generate_words_after_replacing_one_char(word):
    words = []
    for i in range(len(word)):
        for char in string.ascii_lowercase:
            words.append(word[:i] + char + word[i+1:])
    return words

def create_frequency_table(data):
    frequency_table = {}
    for line in data[1:]:  # skip header
        if not line.strip():
            continue
        word, count = line.strip().split(',')
        frequency_table[word.lower()] = int(count)
    return frequency_table

def create_bloom_filter(data):
    bloom_filter = BloomFilter(1000, 0.01)
    for line in data:
        if not line.strip():
            continue
        word = line.strip()
        bloom_filter.add(word)
    return bloom_filter

def persist_bloom_filter(bloom_filter):
    with open('bloom_filter.pkl', 'wb') as f:
        """The first four bytes will be an identifier, we’ll use CCBF.
        The next two bytes will be a version number to describe the version number of the file.
        The next two bytes will be the number of hash functions used.
        The next four bytes will be the number of bits used for the filter.
"""
        f.write(b'CCBF')
        f.write(b'01')
        f.write(bloom_filter.hash_count.to_bytes(2, 'big'))
        f.write(bloom_filter.size.to_bytes(4, 'big'))
        f.write(bytes(bloom_filter.bit_array))

def load_bloom_filter():
    with open('bloom_filter.pkl', 'rb') as f:
        f.read(4)
        f.read(2)
        hash_count = int.from_bytes(f.read(2), 'big')
        size = int.from_bytes(f.read(4), 'big')
        bit_array = f.read(size)
        bloom_filter = BloomFilter(1000, 0.01)
        bloom_filter.bit_array = bytearray(bit_array)
        bloom_filter.hash_count = hash_count
        bloom_filter.size = size
        return bloom_filter

def generate_words_after_transposing_two_chars(word):
    words = []
    for i in range(len(word)-1):
        char_i = word[i]
        char_j = word[i+1]
        words.append(word[:i]+char_j+char_i+word[i+2:])
    return words

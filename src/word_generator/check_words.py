
from src.word_generator.generate_words import load_bloom_filter
import argparse
import random
import string

def load_bloom_filter_from_disk(file_path):
    bloom_filter = load_bloom_filter()

    with open(file_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            print(line.strip(), bloom_filter.check(line.strip()))

    false_positives = 0
    trials = 20000

    def random_word():
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    for i in range(trials):
        word = random_word()
        if bloom_filter.check(word):
            print(word)
            false_positives += 1

    print("FP rate:", false_positives / trials)

if __name__ == "__main__":  
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file_path", help="Path to the file")
    args = arg_parser.parse_args()
    load_bloom_filter_from_disk(args.file_path)
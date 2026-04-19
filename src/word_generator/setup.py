from src.word_generator.generate_words import create_bloom_filter, persist_bloom_filter
import argparse

def read_data(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def setup(file_path):
    data = read_data(file_path)
    bloom_filter = create_bloom_filter(data)
    persist_bloom_filter(bloom_filter)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file_path", help="Path to the file")
    args = arg_parser.parse_args()
    setup(args.file_path)
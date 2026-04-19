from src.word_generator.generate_words import load_bloom_filter,generate_words_after_deleting_one_char, generate_words_after_inserting_one_char, generate_words_after_replacing_one_char, generate_words_after_transposing_two_chars
from collections import defaultdict

class SpellChecker:
    def __init__(self, data):
        self.bloom_filter = load_bloom_filter()

    def correct_word(self, input_word):
        if self.bloom_filter.check(input_word):
            return input_word
        else:
            one_off_words = self.create_one_off_words(input_word)
            word_with_highest_frequency = max(one_off_words, key=lambda x: self.bloom_filter.check(x))
            # print(word_with_highest_frequency, self.frequency_table.get(word_with_highest_frequency, 0))
            if self.frequency_table.get(word_with_highest_frequency, 0) > 0:
                return word_with_highest_frequency
            else:
                two_off_words = []
                for word in one_off_words:
                    two_off_words.extend(self.create_one_off_words(word))
                word_with_highest_frequency = max(two_off_words, key=lambda x: self.bloom_filter.check(x))
                # print(word_with_highest_frequency, self.frequency_table.get(word_with_highest_frequency, 0))
                if self.bloom_filter.check(word_with_highest_frequency):
                    return word_with_highest_frequency
                else:
                    return input_word
    
    def create_one_off_words(self, word):
        return generate_words_after_deleting_one_char(word) + generate_words_after_inserting_one_char(word) + generate_words_after_replacing_one_char(word) + generate_words_after_transposing_two_chars(word)


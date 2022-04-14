from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):
    def __init__(self):
        self.data = {}

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.data = {entry.word: entry.frequency for entry in words_frequencies}

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        return self.data.get(word, 0)

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        freq = self.search(word_frequency.word)
        if freq > 0:
            return False
        else:
            self.data[word_frequency.word] = word_frequency.frequency
            return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        freq = self.search(word)
        if freq > 0:
            del self.data[word]
            return True
        else:
            return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # Find the keys that start with a given prefix
        autoDic = {key: freq for key, freq in self.data.items() if key.startswith(word)}
        # Use Python's built-in sorting algorithm to sort autoDic by frequency and return the last three elements in descending order.
        return [WordFrequency(key, freq) for key, freq in sorted(autoDic.items(), key=lambda item: item[1], reverse=True)][:3]

from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):
    def __init__(self):
        self.data: list = None;

    # merge sort algorithm sourced from Zybooks
    def merge(self, data, i, j, k):
        merged_size = k - i + 1  # Size of merged partition
        merged_data = [0] * merged_size  # Dynamically allocates temporary array
        # for merged numbers
        merge_pos = 0  # Position to insert merged number
        left_pos = i  # Initialize left partition position
        right_pos = j + 1  # Initialize right partition position

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= j and right_pos <= k:
            if data[left_pos].word <= data[right_pos].word:
                merged_data[merge_pos] = data[left_pos]
                left_pos += 1
            else:
                merged_data[merge_pos] = data[right_pos]
                right_pos += 1
            merge_pos = merge_pos + 1

        # If left partition is not empty, add remaining elements to merged numbers
        while left_pos <= j:
            merged_data[merge_pos] = data[left_pos]
            left_pos += 1
            merge_pos += 1

        # If right partition is not empty, add remaining elements to merged numbers
        while right_pos <= k:
            merged_data[merge_pos] = data[right_pos]
            right_pos = right_pos + 1
            merge_pos = merge_pos + 1

        # Copy merge number back to numbers
        for merge_pos in range(merged_size):
            data[i + merge_pos] = merged_data[merge_pos]

    def merge_sort(self, data, i, k):
        j = 0

        if i < k:
            j = (i + k) // 2  # Find the midpoint in the partition

            # Recursively sort left and right partitions
            self.merge_sort(data, i, j)
            self.merge_sort(data, j + 1, k)

            # Merge left and right partition in sorted order
            self.merge(data, i, j, k)

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.data = words_frequencies
        # Merge-sort data (The time complexity of nlogn)
        self.merge_sort(self.data, 0, len(self.data) - 1)

    def binSearch(self, word:str) -> int:
        """
        binary search for a word
        @param word: the word to be searched
        @return: the index of word_frequencies if found -1 if not.
        """
        low, high = 0, len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.data[mid].word > word:
                high = mid - 1
            elif self.data[mid].word < word:
                low = mid + 1
            else:
                return mid
        return -1

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # Employ binary search
        index = self.binSearch(word)
        if index == -1:
            return 0
        else:
            return self.data[index].frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return []

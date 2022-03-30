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
    def merge(self, data, i, j, k, by: str):
        merged_size = k - i + 1  # Size of merged partition
        merged_data = [0] * merged_size  # Dynamically allocates temporary array
        # for merged numbers
        merge_pos = 0  # Position to insert merged number
        left_pos = i  # Initialize left partition position
        right_pos = j + 1  # Initialize right partition position

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= j and right_pos <= k:
            if getattr(data[left_pos], by) <= getattr(data[right_pos], by):
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

    def merge_sort(self, data, i, k, by: str):
        j = 0

        if i < k:
            j = (i + k) // 2  # Find the midpoint in the partition

            # Recursively sort left and right partitions
            self.merge_sort(data, i, j, by)
            self.merge_sort(data, j + 1, k, by)

            # Merge left and right partition in sorted order
            self.merge(data, i, j, k, by)

    def __str__(self):
        str = ""
        for items in self.data:
            str += f"({items.word}, {items.frequency})\n"
        return str

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.data = words_frequencies
        # Merge-sort data (The time complexity of nlogn)
        self.merge_sort(self.data, 0, len(self.data) - 1, "word")

    def binSearch(self, word:str) -> (bool, int):
        """
        binary search for a word
        @param word: the word to be searched
        @return: (True, the index of word_frequencies) OR (False, the index of word_frequencies to be inserted into)
        """
        low, mid, high = 0, 0, len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.data[mid].word > word:
                high = mid - 1
            elif self.data[mid].word < word:
                low = mid + 1
            else:
                return (True, mid)
        return (False, mid)

    def binSearchAC(self, prefix_word:str) -> int:
        """
        binary search for a prefix
        @param prefix: the prefix to be searched
        @return: if found: the index of the first encountered word with the same prefix; if not: -1
        """
        # The implementation is almost identical to binSearch except that prefix is compared to word upto its own length
        low, mid, high = 0, 0, len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.data[mid].word[:len(prefix_word)] > prefix_word:
                high = mid - 1
            elif self.data[mid].word[:len(prefix_word)] < prefix_word:
                low = mid + 1
            else:
                return mid
        return -1

    def getAutocompleteList(self, prefix_word: str, idx: int) -> [WordFrequency]:
        """
        add all the words sharing the same prefix_word to a list and return it unsorted
        @param prefix_word: the prefix_word to be searched, idx: the starting index to search from in both directions (left and right)
        @return: an unsorted list containing all the words sharing the same prefix_word
        """
        res = []
        # Add the first word
        res.append(self.data[idx])
        left_idx = idx - 1
        right_idx = idx + 1

        if left_idx >= 0:
            curr_left_word = self.data[left_idx].word[:len(prefix_word)]
        # Add words to the left of the first word
        while left_idx >= 0 and curr_left_word == prefix_word:
            res.append(self.data[left_idx])
            left_idx -= 1
            curr_left_word = self.data[left_idx].word[:len(prefix_word)]

        if right_idx <= len(self.data) - 1:
            curr_right_word = self.data[right_idx].word[:len(prefix_word)]
        # Add words to the right of the first word
        while right_idx <= len(self.data) - 1 and curr_right_word == prefix_word:
            res.append(self.data[right_idx])
            right_idx += 1
            curr_right_word = self.data[right_idx].word[:len(prefix_word)]

        return res

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # Employ binary search
        isFound, foundIdx = self.binSearch(word)
        if not isFound:
            return 0
        else:
            return self.data[foundIdx].frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Employ binary search
        word = word_frequency.word
        isFound, foundIdx = self.binSearch(word)
        actualLength = len(self.data)
        if isFound:
            return False
        # If not found, add the word in self.data
        else:
            # Create space to shuffle elements to the right by 1
            self.data.append(None)
            for i in range(actualLength - 1, foundIdx - 1, -1):
                self.data[i + 1] = self.data[i]
            self.data[foundIdx] = word_frequency
            return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        isFound, foundIdx = self.binSearch(word)
        if isFound:
            for i in range(foundIdx, len(self.data) - 1):
                self.data[i] = self.data[i + 1]
            # In all cases, the last element will be deleted if the word is found
            del self.data[-1]
            return True
        # If found, delete the word in self.data
        else:
            return False



    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # As soon as prefix_word matches with any word, scan all the words to its left and right and put them in a new list
        # Iterate them only once to find the 3 most-frequent words
        idx = self.binSearchAC(prefix_word)
        if idx == -1:
            return []
        else:
            lst = self.getAutocompleteList(prefix_word, idx)
            self.merge_sort(lst, 0, len(lst) - 1, "frequency")
            return lst[-3:][::-1]

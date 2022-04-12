from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):
    def __init__(self):
        self.root = Node()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for idx, entry in enumerate(words_frequencies):
            self.add_word_frequency(entry)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        endNode = self.search_from_node(self.root, word, 0)
        if endNode == None:
            return 0
        elif endNode.end_word == False:
            return 0
        else:
            return endNode.frequency



    def search_from_node(self, currNode, word, currIdx):
        """
        search for a word recursively
        @param node, word, currIdx: node to start from, the word to be searched, currIdx to search curLetter at
        @return: frequency > 0 if found and 0 if NOT found
        """
        currLetter = word[currIdx]
        if currNode == None or currNode.letter == None:
            return None
        if currNode.letter < currLetter:
            return self.search_from_node(currNode.right, word, currIdx)
        elif currNode.letter > currLetter:
            return self.search_from_node(currNode.left, word, currIdx)
        elif currIdx < len(word) - 1:
            return self.search_from_node(currNode.middle, word, currIdx + 1)
        else:
            return currNode


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        return self.add_word_from_root(self.root, word_frequency.word, word_frequency.frequency, 0)

    def add_word_from_root(self, currNode, word, freq, currIdx) -> bool:
        """
        add a word recursively
        @param currNode, word, freq, currIdx: currNode initially self.root; currIdx is used for the base case.
        :return: True if addition is successful, false if the word being added already exists.
        """
        currLetter = word[currIdx]
        # Base case on the last word
        if currIdx == len(word) - 1:
            if currNode.letter == None:
                currNode.letter = currLetter
                currNode.frequency = freq
                currNode.end_word = True
                return True
            # If currNode is the same as curLetter
            else:
                if currNode.letter > currLetter:
                    if currNode.left == None:
                        currNode.left = Node()
                    currNode = currNode.left
                    return self.add_word_from_root(currNode, word, freq, currIdx)
                elif currNode.letter < currLetter:
                    if currNode.right == None:
                        currNode.right = Node()
                    currNode = currNode.right
                    return self.add_word_from_root(currNode, word, freq, currIdx)
                else:
                    if currNode.end_word == True:
                        return False
                    else:
                        currNode.frequency = freq
                        currNode.end_word = True
                        return True
        # Recursive case
        else:
            # When no word is present
            if currNode.letter == None:
                currNode.letter = currLetter
                currNode.middle = Node()
                currNode = currNode.middle
                return self.add_word_from_root(currNode, word, freq, currIdx + 1)
            elif currNode.letter < currLetter:
                if currNode.right == None:
                    currNode.right = Node()
                currNode = currNode.right
                return self.add_word_from_root(currNode, word, freq, currIdx)
            elif currNode.letter > currLetter:
                if currNode.left == None:
                    currNode.left = Node()
                currNode = currNode.left
                return self.add_word_from_root(currNode, word, freq, currIdx)
            else:
                if currNode.middle == None:
                    currNode.middle = Node()
                currNode = currNode.middle
                return self.add_word_from_root(currNode, word, freq, currIdx + 1)

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # First, search for a word
        # endNode = self.search_from_node(self.root, word, 0)
        # if not endNode or endNode.end_word == False:
        #     return False
        # else:
        #     endNode.frequency = None
        #     endNode.end_word = False
        #     if endNode.left == None and endNode.middle == None and endNode.right == None:
        #         del endNode
        # return True
        deleteStatus = [False]
        self.delete_from_node(self.root, word, 0, deleteStatus)
        return deleteStatus[0]

    def delete_from_node(self, currNode, word, currIdx, deleteStatus: list[bool]):
        """
        delete a word recursively
        @param prevNode, currNode, word, currIdx
        @return: False if not found or end_word equals False, True if found and end_word equals True
        """
        currLetter = word[currIdx]
        if currNode == None or currNode.letter == None:
            return False
        if currNode.letter < currLetter:
            if self.delete_from_node(currNode.right, word, currIdx, deleteStatus):
                currNode.right = None
            else:
                return False
        elif currNode.letter > currLetter:
            if self.delete_from_node(currNode.left, word, currIdx, deleteStatus):
                currNode.left = None
            else:
                return False
        elif currIdx < len(word) - 1:
            if self.delete_from_node(currNode.middle, word, currIdx + 1, deleteStatus):
                currNode.middle = None
            else:
                return False
        else:
            if currNode.end_word:
                deleteStatus[0] = True
                currNode.frequency = None
                currNode.end_word = False

        if currNode.end_word == False:
            if currNode.left == None and currNode.middle == None and currNode.right == None:
                return True
            else:
                return False
        else:
            return False

    def add_ac_words(self, currNode: Node, compoundWord: str, ac_lst: list) -> [WordFrequency]:
        """
        Recursively traverse all the children nodes of currNode and create an instance of WordFrequency
        using compoundWord and the frequency of currNode if its end_word is True.
        @param currNode, compoundWord, ac_lst: compoundWord to keep track of the word to be added
        ac_lst: the list to which an instance of WordFrequency is added
        @return: a list (could be empty) of all the words with prefix 'word'
        """

        # Base Case 1: currNode is None
        if currNode == None:
            return
        # Recursive case:
        else:
            if currNode.end_word == True:
                ac_lst.append(WordFrequency(compoundWord + currNode.letter, currNode.frequency))
            self.add_ac_words(currNode.left, compoundWord, ac_lst)
            self.add_ac_words(currNode.middle, compoundWord + currNode.letter, ac_lst)
            self.add_ac_words(currNode.right, compoundWord, ac_lst)

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # a list of words to be autocompleted
        ac_lst = []

        # Find the prefix
        currNode = self.search_from_node(self.root, word, 0)

        # If the prefix does not exist
        if not currNode:
            return ac_lst
        else:
            # If the currNode's end_word is true
            if currNode.end_word == True:
                ac_lst.append(WordFrequency(word, currNode.frequency))
            self.add_ac_words(currNode.middle, word, ac_lst)

            # Python's built-in Timsort
            ac_lst.sort(key=lambda wordFrequency: wordFrequency.frequency, reverse=True)

        return ac_lst[:3]

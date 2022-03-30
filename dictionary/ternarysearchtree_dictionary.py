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
        # Initiate the root node
        # first_word = words_frequencies[0].word
        # if self.root == None:
        #     self.root = Node(first_word[0], # The first letter of the first word
        #                      first_word.frequency if len(first_word) == 1 else None, # If thee first word isn't length 1, set frequency to None
        #                      True if len(first_word) == 1 else False) # if the first word is length 1, set end_word to True
        for idx, entry in enumerate(words_frequencies):
            self.add_word_frequency(entry)
        print('finished')

    # def letterExistsInChildrenNodes(self, node, letter) -> (bool, Node):
    #     """
    #     checks whether the letter in search exists in the node's left, middle, or right.
    #     @param node, letter: letter to check if it exists in node's children
    #     @return: false, node to store the letter if not, true, node where the letter is found if found in any one of them
    #     """
    #
    #     if node.middle.letter == letter:
    #         return (True, node.middle)
    #     if node.left.letter < letter: # If node's letter is less than letter e.g. c < f
    #         return self.letterExistsInChildrenNodes()
    #     if node.right.letter == letter: # If node's letter is greater than letter e.g. c < a
    #         return True
    #     return False


    # def search(self, word: str) -> int:
    #     """
    #     search for a word
    #     @param word: the word to be searched
    #     @return: frequency > 0 if found and 0 if NOT found
    #     """
    #     currNode = self.root
    #     for letter in word:
    #         if currNode == None:
    #             return 0
    #         currNode = self.search_from_node(currNode, letter)
    #
    #     return 0
    #
    # def search_from_node(self, node, letter):
    #     if node == None:
    #         return None
    #     else:
    #         if node.letter == letter:
    #             return node.middle
    #         elif node.letter < letter: # If the node's letter is less than the letter searched for e.g. c < f
    #             return node.right
    #         else:
    #             return node.left






    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Search first the node in which the letter is stored.
        # node = self.root
        # for letter in word_frequency.word[:-1]:
        #     node = self.add_letter(node, letter)
        # node = self.add_letter(node, word_frequency.word[-1], word_frequency.frequency, end_word=True)
        #
        # if node:
        #     return True
        # else:
        #     return False
        self.add_word(self.root, word_frequency.word, word_frequency.frequency, 0)


    def add_word(self, currNode, word, freq, currIdx) -> bool:
        """
        add a word
        @param root, word:
        :return: root
        """
        currLetter = word[currIdx]
        if currIdx == len(word) - 1:
            if currNode.letter == None:
                currNode.letter = currLetter
                currNode.freq = freq
                currNode.end_word = True
                return True
            else:
                # If currNode is the same as curLetter
                if currNode.letter > currLetter:
                    if currNode.left == None:
                        currNode.left = Node()
                    currNode = currNode.left
                    self.add_word(currNode, word, freq, currIdx)
                elif currNode.letter < currLetter:
                    if currNode.right == None:
                        currNode.right = Node()
                    currNode = currNode.right
                    self.add_word(currNode, word, freq, currIdx)
                else:
                    if currNode.end_word == True:
                        return False
                    else:
                        currNode.end_word = True
                        return True
        else:
            if currNode.letter == None:
                currNode.letter = currLetter
                currNode.middle = Node()
                currNode = currNode.middle
                self.add_word(currNode, word, freq, currIdx + 1)
            elif currNode.letter < currLetter:
                if currNode.right == None:
                    currNode.right = Node()
                currNode = currNode.right
                self.add_word(currNode, word, freq, currIdx)
            elif currNode.letter > currLetter:
                if currNode.left == None:
                    currNode.left = Node()
                currNode = currNode.left
                self.add_word(currNode, word, freq, currIdx)
            else:
                if currNode.middle == None:
                    currNode.middle = Node()
                currNode = currNode.middle
                self.add_word(currNode, word, freq, currIdx + 1)






        # # Check whether the letter can be found in any of the children
        # if node.left.letter == letter:
        #     pass
        # elif node.middle.letter == letter:
        #     pass
        # elif node.right.letter == letter:
        #     pass
        # # If none of the node's children contains the letter
        # else:
        #     # If node.middle doesn't exist
        #     if not node.middle:
        #         node.middle = Node(letter, frequency, end_word)
        #         return node.middle
        #     else:
        #         # If node's middle child's letter is greater than letter to add e.g. c > a
        #         if node.middle.letter > letter:
        #             return self.add_letter(node.mid, letter, frequency, end_word)
        #         else:
        #             return self.add_letter(node.mid, letter, frequency, end_word)


            # if node.letter == letter:
            #     # Code executed before exit
            #     if (end_word == True):
            #
            #             return None
            #         else:
            #             node.frequency = frequency
            #             node.end_word = end_word
            #             return node
            #     return node.middle
            # elif node.letter > letter:
            #     return self.add_letter(node.left, letter)
            # else:
            #     return self.add_letter(node.right, letter)



    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return []

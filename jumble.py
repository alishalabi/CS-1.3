from set_hashtable import Set
from itertools import permutations


class Jumble(object):
    def __init__(self, jumbled_word):
        self.jumbled_word = jumbled_word
        self.perm_set = Set(500)
        self.dictionary_words =

    def find_permuations(self):
        """
        Run code to generate every possible permutation of the jumble,
        add each permutation to perm_set
        """
        perms = [''.join(p) for p in permutations(self.jumbled_word)]
        for perm in perms:
            self.perm_set.add(perm)
        print(self.perm_set)


newJumble = Jumble("tefon")

newJumble.find_permuations()

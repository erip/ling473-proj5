#!/usr/bin/env python3

import operator
from functools import reduce

class Model(object):
    def __init__(self, counts):
        self.counts = counts

    def _total_word_count(self):
        return sum(self.counts.values())

    def _highest_probability(self):
        return max(self.counts.values())

    def _lowest_probability(self):
        return min(self.counts.values())

    def update_prior(self, word):
        self.counts[word] = self.counts.get(word, 0) + 1

    def get_word(self, word):
        return self.counts.get(word, self._lowest_probability())

    def get_probability_of_word(self, word):
        return self.get_word(word) / self._total_word_count()

    def process_sentence(self, toks):
        res = reduce(operator.add, map(self.get_probability_of_word, toks), 0)
        return res

#!/usr/bin/env python3

import string
import numpy as np

class NaiveBayesClassifier(object):
    def __init__(self, models, verbose=False):
        self.models = models
        self.verbose = verbose

    def train(self, lang, sentences):
        for sentence in sentences:
            words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
            for word in words:
                self.models[lang].update_prior(word)

    def predict(self, text):
        words = text.translate(str.maketrans('', '', string.punctuation)).split()
        preds = {lang: -np.log10(model.process_sentence(words)) for lang, model in self.models.items()}
        if self.verbose:
            for (lang, score) in preds.items():
                print("{0}\t{1}".format(lang, score))
        return min(preds, key=preds.get)


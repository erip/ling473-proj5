#!/usr/bin/env python3

import os
import codecs
from model_reader import ModelReader
from naive_bayes import NaiveBayesClassifier

def train(nb, file):
    correct = 0
    count = 0
    with codecs.open(file, 'r', encoding=ModelReader.encoding) as f:
        for line in f:
            count += 1
            lang, sent = line.strip().split("\t")
            pred_lang = nb.predict(sent)
            print("Predicted {0}, actual {1}".format(pred_lang, lang))
            correct += (pred_lang == lang)
    print("Accuracy: {0}".format(correct / count))

def test(nb, file):
    with codecs.open(file, 'r', encoding=ModelReader.encoding) as f:
        for line in f:
            _, sent = line.strip().split("\t")
            pred_lang = nb.predict(sent)
            print("Predicted '{0}' for '{1}'".format(pred_lang, sent))

if __name__ == "__main__":
    test_pass = True

    dir = "/opt/dropbox/17-18/473/project5/language-models"
    files = [os.path.abspath(os.path.join(dir, file)) for file in os.listdir(dir)]
    lang_file_pairs = { file.split(".")[0][-3:]: ModelReader(file).get() for file in files }
    nb = NaiveBayesClassifier(lang_file_pairs, verbose=True)

    if test_pass:
        test(nb, "/opt/dropbox/17-18/473/project5/test.txt")
    else:
        train(nb, "/opt/dropbox/17-18/473/project5/train.txt")
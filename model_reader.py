#!/usr/bin/env python3

import codecs
from model import Model

class ModelReader(object):
    encoding = 'ISO-8859-1'
    def __init__(self, filename):
        self.model = self._read(filename)

    def get(self):
        return Model(self.model)

    @classmethod
    def _process_line(cls, line):
        k, v = line.encode(ModelReader.encoding).decode(ModelReader.encoding).split("\t")
        return (k, int(v))

    @classmethod
    def _read(cls, filename):
        with codecs.open(filename, encoding=ModelReader.encoding) as f:
            return {k: v for (k, v) in map(cls._process_line, f)}


#!/usr/bin/env python

from pokegen_i import PokeGenI
from pokegen_ii import PokeGenII

class PokeCodec:

    def __init__(self, gen, reduce, min_len):
        self.reduce = reduce
        self.min_len = min_len

        if gen == 1:
            self.poke = PokeGenI()
        elif gen == 2:
            self.poke = PokeGenII()
        else:
            raise ValueError(f"Gen{gen} unsupported")

        self.decodings = self.poke.getDecodings()
        self.codes = self.poke.getPokeCodes()

    def getPokeCodes(self):
        return self.codes

    def decode(self, data):
        if self.reduce:
            # discard large lists of 0xff (encoding for '9')
            prev = None
            data = [prev := v for v in data if v != 0xff and prev != v]
            if len(data) < self.min_len:
                return

        for d in data:
            if d in self.decodings:
                print(self.decodings[d], end="")
            else:
                print("?", end="")
        print()

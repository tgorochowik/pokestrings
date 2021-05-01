#!/usr/bin/env python

from .utils import get_pokegen


class PokeCodec:
    def __init__(self, gen, e_acute):
        poke = get_pokegen(gen)

        self.encodings = poke.get_encodings()
        self.codes = poke.get_pokecodes()

        if e_acute:
            self.encodings.update(self.poke.get_e_acute_encodings())

    def decode(self, data):
        answer = ""
        for d in data:
            if d in self.encodings:
                answer += self.encodings[d]
            else:
                answer += "_"
        return answer

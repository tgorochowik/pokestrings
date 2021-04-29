#!/usr/bin/env python

import string

from .pokegen import PokeGen


class PokeGenI(PokeGen):
    def __init__(self):
        upper = dict(zip(list(range(0x80, 0x9a)), string.ascii_uppercase))
        lower = dict(zip(list(range(0xa0, 0xba)), string.ascii_lowercase))
        digits = dict(zip(list(range(0xf6, 0x100)), string.digits))

        # add special entries
        self.encodings = {
            # junk at 0x00-0x47
            # control chars at 0x48-0xx5f
            0x4a: "PkMn",
            0x52: "<player>",
            0x53: "<rival>",
            0x54: "Poke",
            0x56: "...",
            0x59: "<target>",
            0x5a: "<user>",
            0x5b: "PC",
            0x5c: "TM",
            0x5d: "TRAINER",
            0x5e: "ROCKET",
            # pokedex only entries
            0x60: "'",
            0x61: "\"",
            # leftovers at 0x60-0x78
            0x6d: ":",
            # text borders at 0x79-0x7e
            0x7f: " ",
            # upper chars at 0x80-0x99
            0x9a: "(",
            0x9b: ")",
            0x9c: ":",
            0x9d: ";",
            0x9e: "[",
            0x9f: "]",
            # lower chars at 0xa0-0xb9
            0xba: "e",  # é
            0xbb: "'d",
            0xbc: "'l",
            0xbd: "'s",
            0xbe: "'t",
            0xbf: "'v",
            # junk at 0xc0 - 0xdf
            0xe0: "'",
            0xe1: "PK",
            0xe2: "MN",
            0xe3: "-",
            0xe4: "'r",
            0xe5: "'m",
            0xe6: "?",
            0xe7: "!",
            0xe8: ".",
            # e9-eb contains leftovers
            0xec: "▷",
            0xed: "▶",
            0xee: "▼",
            0xef: "♂",
            0xf0: "$",
            0xf1: "x",
            0xf2: ".",
            0xf3: "/",
            0xf4: ",",
            0xf5: "♀",
            # 0xf6-0xff contains digits
        }
        self.encodings.update(upper)
        self.encodings.update(lower)
        self.encodings.update(digits)

        self.pokecodes = list(self.encodings.keys())

import string

from .pokegen import PokeGen


class PokeGenII(PokeGen):
    def __init__(self):
        upper = dict(zip(list(range(0x80, 0x9a)), string.ascii_uppercase))
        lower = dict(zip(list(range(0xa0, 0xba)), string.ascii_lowercase))
        digits = dict(zip(list(range(0xf6, 0x100)), string.digits))

        # add special entries
        self.encodings = {
            # junk at 0x00-0x47
            # control chars at 0x48-0x5f
            0x4a: "PkMn",
            0x52: "<player>",
            0x53: "<rival>",
            0x54: "Poke",
            0x56: "......",
            0x59: "<inactive_pokemon>",
            0x5a: "<active_pokemon>",
            0x5b: "PC",
            0x5c: "TM",
            0x5d: "TRAINER",
            0x5e: "ROCKET",
            0x60: "■",
            0x61: "▲",
            0x62: "<phone_icon>",
            # mostly artifacts at 0x60-0x78
            0x70: "PO",
            0x71: "KE",
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
            # leftovers
            0xd0: "'d",
            0xd1: "'l",
            0xd2: "'m",
            0xd3: "'r",
            0xd4: "'s",
            0xd5: "'t",
            0xd6: "'v",
            # junk
            0xdf: "←",
            # junk at 0xc0 - 0xdf
            0xe0: "'",
            0xe1: "PK",
            0xe2: "MN",
            0xe3: "-",
            # leftovers
            0xe6: "?",
            0xe7: "!",
            0xe8: ".",
            0xe9: "&",
            0xea: "e",  # é
            0xeb: "→",
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

        # encodings using é (overwrite the above if needed)
        self.e_acute_encodings = {
            0x54: "Poké",
            0xea: "é",
        }

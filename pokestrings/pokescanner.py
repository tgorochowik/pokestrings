from .utils import get_pokegen


class PokeScanner:
    def __init__(self, gen, reduce, min_len):
        self.reduce = reduce
        self.min_len = min_len

        poke = get_pokegen(gen)

        self.pokecodes = poke.get_pokecodes()

    def scan(self, data):
        pos = 0
        while pos < len(data):
            matches = 0
            match = 0
            if data[pos] in self.pokecodes:
                match = pos
                matches = 1
                while pos + matches < len(data) and data[
                        pos + matches] in self.pokecodes:
                    matches += 1

                offset = pos
                match = data[pos:pos + matches]

                if self.reduce:
                    prev = None
                    reduced = [
                        prev := v for v in match
                        if v != 0xff or (v == 0xff and prev != v)
                    ]

                    # recalculate offset in case anything was reduced in the front
                    offset += match.index(reduced[0])
                    match = reduced
                    del reduced

                if len(match) >= self.min_len:
                    yield (offset, match)
                pos += matches
            else:
                pos += 1

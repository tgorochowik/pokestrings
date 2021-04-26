#!/usr/bin/env python3

import string
import sys

pokechars = string.ascii_uppercase + "():;[]" + string.ascii_lowercase + "edlstv" + "'??-rm?!.___▷▶▼♂$x./,♀0123456789"
pokecodes = list(range(0x80, 0xc0)) + list(range(0xe0, 0x100))

decodings = dict(zip(pokecodes, pokechars))


def decode(data):
    # discard large lists of 0xff (encoding for '9')
    prev = None
    data = [prev := v for v in data if v != 0xff and prev != v]
    if len(data) < 3:
        return

    for d in data:
        if d in decodings:
            print(decodings[d], end="")
        else:
            print("?", end="")
    print()


data = []

with open(sys.argv[1], "rb") as f:
    data = f.read()

pos = 0

while pos < len(data):
    matches = 0
    match = 0
    if data[pos] in pokecodes:
        match = pos
        matches = 1
        while pos + matches < len(data) and data[pos + matches] in pokecodes:
            matches += 1
        if matches >= 3:
            decode(data[pos:pos + matches])
        pos += matches
    else:
        pos += 1

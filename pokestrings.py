#!/usr/bin/env python3

import sys
import argparse
from pokecodec import PokeCodec

parser = argparse.ArgumentParser(description='Extract strings from Pokemon ROMs.')

parser.add_argument('--generation',
                    '-g',
                    type=int,
                    default=1,
                    required=False,
                    help='Game generation')

parser.add_argument('--minimum-length',
                    '-l',
                    type=int,
                    default=3,
                    required=False,
                    help='Minimum number of consecutive characters to be considered')

parser.add_argument('--no-reduce',
                    dest='reduce',
                    action='store_false',
                    required=False,
                    help='Do not reduce multtiple consective 0xff chars (encoding for 9) to a single char')

parser.add_argument("file", type=str)

args = parser.parse_args()

print(args.reduce)

try:
    codec = PokeCodec(args.generation, args.reduce, args.minimum_length)
except ValueError as e:
    print(e)
    sys.exit(1)

try:
    with open(args.file, "rb") as f:
        data = f.read()
except OSError as e:
    print(e)
    sys.exit(e.errno)

pokecodes = codec.getPokeCodes()

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
            codec.decode(data[pos:pos + matches])
        pos += matches
    else:
        pos += 1

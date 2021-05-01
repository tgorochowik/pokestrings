#!/usr/bin/env python3

import sys
import argparse
from .pokecodec import PokeCodec


def run(args):
    try:
        codec = PokeCodec(args.generation, args.reduce, args.bytes)
    except ValueError as e:
        print(e)
        sys.exit(1)

    try:
        with open(args.file, "rb") as f:
            data = f.read()
    except OSError as e:
        print(e)
        sys.exit(e.errno)

    pokecodes = codec.get_pokecodes()

    pos = 0
    while pos < len(data):
        matches = 0
        match = 0
        if data[pos] in pokecodes:
            match = pos
            matches = 1
            while pos + matches < len(data) and data[pos +
                                                     matches] in pokecodes:
                matches += 1
            if matches >= 3:
                codec.decode(data[pos:pos + matches])
            pos += matches
        else:
            pos += 1


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Extract strings from Pokemon ROMs.')

    parser.add_argument(
        '--generation',
        '-g',
        type=int,
        default=1,
        required=False,
        help='Game Generation, supported generations: 1 (GB), 2 (GBC)')

    parser.add_argument(
        '--bytes',
        '-n',
        type=int,
        default=4,
        required=False,
        help='Number of minimum consecutive characters to be printed')

    parser.add_argument(
        '--no-reduce',
        dest='reduce',
        action='store_false',
        required=False,
        help='Do not reduce multiple consecutive 0xff chars (encoding for 9)')

    parser.add_argument("file", type=str)

    return parser.parse_args()


def main():
    run(parse_args())


if __name__ == "__main__":
    main()

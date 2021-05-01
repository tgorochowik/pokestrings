#!/usr/bin/env python3

import sys
import argparse
from .pokecodec import PokeCodec
from .pokescanner import PokeScanner


def run(args):
    try:
        codec = PokeCodec(args.generation, args.e_acute)
        scanner = PokeScanner(args.generation, args.reduce, args.bytes)
    except ValueError as e:
        print(e)
        sys.exit(1)

    try:
        with open(args.file, "rb") as f:
            data = f.read()
    except OSError as e:
        print(e)
        sys.exit(e.errno)

    for offset, match in scanner.scan(data):
        if args.show_offset:
            print(f"0x{offset:06x}: {codec.decode(match)}")
        else:
            print(codec.decode(match))


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Extract strings from Pokemon ROMs.")

    # yapf: disable
    parser.add_argument(
        "--generation",
        "-g",
        type=int,
        default=1,
        required=False,
        help="Game Generation, supported generations: 1 (GB), 2 (GBC)")

    parser.add_argument(
        "--bytes",
        "-n",
        type=int,
        default=4,
        required=False,
        help="Number of minimum consecutive characters to be printed")

    parser.add_argument(
        "--show-offset",
        "-o",
        action="store_true",
        required=False,
        default=False,
        help="Print the offset before each string")

    parser.add_argument(
        "--e-acute",
        "-e",
        action="store_true",
        required=False,
        default=False,
        help="Do not convert é to regular e")

    parser.add_argument(
        "--no-reduce",
        dest="reduce",
        action="store_false",
        required=False,
        help="Do not reduce multiple consecutive 0xff chars (encoding for 9)")

    parser.add_argument("file", type=str)
    # yapf: enable

    return parser.parse_args()


def main():
    run(parse_args())


if __name__ == "__main__":
    main()

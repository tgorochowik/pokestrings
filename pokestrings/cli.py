#!/usr/bin/env python3

import sys
import argparse
from .pokecodec import PokeCodec
from .pokescanner import PokeScanner


def run_pokestrings(args):
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


def parse_args_pokestrings():
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
        help="game generation, supported generations: 1 (GB), 2 (GBC)")

    parser.add_argument(
        "--bytes",
        "-n",
        type=int,
        default=4,
        required=False,
        help="number of minimum consecutive characters to be printed")

    parser.add_argument(
        "--show-offset",
        "-o",
        action="store_true",
        required=False,
        default=False,
        help="print the offset before each string")

    parser.add_argument(
        "--e-acute",
        "-e",
        action="store_true",
        required=False,
        default=False,
        help="do not convert é to regular e")

    parser.add_argument(
        "--no-reduce",
        dest="reduce",
        action="store_false",
        required=False,
        help="do not reduce multiple consecutive 0xff chars (encoding for 9)")

    parser.add_argument("file", type=str)
    # yapf: enable

    return parser.parse_args()


def run_pokecodec(args):
    try:
        codec = PokeCodec(args.generation, True)
    except ValueError as e:
        print(e)
        sys.exit(1)

    if args.decode:
        print(codec.decode(bytearray.fromhex(args.data)))
        return

    if args.encode:
        print(codec.encode(args.data).hex())
        return


def parse_args_pokecodec():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Decode and encode Pokemon strings.")

    # yapf: disable
    parser.add_argument(
        "--generation",
        "-g",
        type=int,
        default=1,
        required=False,
        help="game generation, supported generations: 1 (GB), 2 (GBC)")

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--decode",
        "-d",
        action="store_true",
        help="hex data to decode")

    mode.add_argument(
        "--encode",
        "-e",
        action="store_true",
        help="string to encode as hex data")

    parser.add_argument("data", type=str)
    # yapf: enable

    return parser.parse_args()


def main_pokestrings():
    run_pokestrings(parse_args_pokestrings())
    sys.exit(0)


def main_pokecodec():
    run_pokecodec(parse_args_pokecodec())
    sys.exit(0)


def main():
    try:
        if "strings" in sys.argv[1]:
            sys.argv = sys.argv[1:]
            main_pokestrings()

        if "codec" in sys.argv[1]:
            sys.argv = sys.argv[1:]
            main_pokecodec()

        raise ValueError("Invalid tool selector")

    except IndexError as e:
        print("Specify tool as the first argument")
    except ValueError as e:
        print(e)

    # should not reach this with valid options
    sys.exit(1)


if __name__ == "__main__":
    main()

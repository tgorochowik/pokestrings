# pokestrings utilities

This repository contains small Pokemon string manipulation utilities.

`pokestrings` can be used to find string sequences in Pokemon ROMs (GB and GBC is supported).

`pokecodec` can be used to encode and decode arbitrary hex sequence to and from Game Boy Pokemon encodings.

## pokestrings

```
$ pokestrings --help
usage: pokestrings [-h] [--generation GENERATION] [--bytes BYTES] [--show-offset] [--e-acute] [--no-reduce] file

Extract strings from Pokemon ROMs.

positional arguments:
  file

  optional arguments:
    -h, --help            show this help message and exit
      --generation GENERATION, -g GENERATION
                              Game Generation, supported generations: 1 (GB), 2 (GBC) (default: 1)
                                --bytes BYTES, -n BYTES
                                                        Number of minimum consecutive characters to be printed (default: 4)
    --show-offset, -o     Print the offset before each string (default: False)
    --e-acute, -e         Do not convert é to regular e (default: False)
    --no-reduce           Do not reduce multiple consecutive 0xff chars (encoding for 9) (default: True)
```

Example usage:

```
$ pokestrings pokered.gbc | grep -i slowpoke -a2
FEAROW
PIDGEY
SLOWPOKE
KADABRA
GRAVELER
--
even now!
We nicknamed the
WARDEN SLOWPOKE.
He and SLOWPOKE
both lok vacant!
SLOWPOKE is very
knowledgeable
about PokeMON!
--
fosils of rare,
extinct PokeMON!
SLOWPOKE came in,
but I couldnt
understand him.
--
young in a pouch
on its bely.
Name: SLOWPOKE
Friendly and very
slow moving.
--
The SHELDER that
is latched onto
SLOWPOKEs tail
is said to fed
on the hosts left
```

## pokecodec

```
pokecodec --help
usage: pokecodec [-h] [--generation GENERATION] (--decode | --encode) data

Decode and encode Pokemon strings.

positional arguments:
  data

  optional arguments:
    -h, --help            show this help message and exit
      --generation GENERATION, -g GENERATION
                              Game Generation, supported generations: 1 (GB), 2 (GBC) (default: 1)
                                --decode, -d          hex data to decode (default: False)
    --encode, -e          string to encode as hex data (default: False)
```

Example usage:

```
$ pokecodec -e "This is awesome!"
93a7a8b27fa8b27fa0b6a4b2aeaca4e7
$ pokecodec -d 93a7a8b27fa8b27fa0b6a4b2aeaca4e7
This is awesome!
```

## Python library

Both the codec and scanner can be used as a library.

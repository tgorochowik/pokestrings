import pytest
import string

from pokestrings import PokeCodec


@pytest.mark.parametrize("gen", [1, 2])
@pytest.mark.parametrize("str_in", [
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.digits,
    "Pokémon",
    "sentence with spaces",
    "?!.$,/",
])
def test_encode_and_decode_produces_the_same_string(gen, str_in):
    c = PokeCodec(gen, True)
    str_out = c.decode(c.encode(str_in))
    assert str_in == str_out, "Encoding and decoding back produced a different result"


@pytest.mark.parametrize("gen", [1, 2])
@pytest.mark.parametrize("unknown_char", ["@", "#"])
def test_unknown_char_produces_an_underscore(gen, unknown_char):
    c = PokeCodec(gen, True)
    result = c.decode(c.encode(unknown_char))
    assert "_" == result, "Unknown char should produce an underscore"


@pytest.mark.parametrize("gen", [1, 2])
@pytest.mark.parametrize("str_in,expected_str_out", [
    ("Pokémon", "Pokemon"),
    ("Pokédex", "Pokedex"),
    ("POKéMON", "POKeMON"),
    ("POKéDEX", "POKeDEX"),
    ("éééé éé", "eeee ee"),
])
def test_disabling_e_acute_strips_it_to_e(gen, str_in, expected_str_out):
    c = PokeCodec(gen, True)
    str_in_encoded = c.encode(str_in)

    c = PokeCodec(gen, False)
    str_out = c.decode(str_in_encoded)
    assert str_out == expected_str_out, "E-acute should be converted to e"

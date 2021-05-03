from .pokegen_i import PokeGenI
from .pokegen_ii import PokeGenII


def get_pokegen(gen):
    if gen == 1:
        return PokeGenI()

    if gen == 2:
        return PokeGenII()

    raise ValueError(f"Gen{gen} unsupported")

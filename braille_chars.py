WIDTH = 2
HEIGHT = 4

bitvec_mask = [ 1, 8, 2, 16, 4, 32, 64, 128 ]

def from_bitvec(bitvec):
    """
    Returns a corresponding unicode braille character to a passed bit vector
    The the respective positions of input bits in the output character are as follows:
    0 3
    1 4
    2 5
    6 7
    """

    return chr(0x2800 + sum(a * b for a, b in zip(bitvec, bitvec_mask)))

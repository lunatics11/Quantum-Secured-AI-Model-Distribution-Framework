import random

def _measure_qubit(bit, alice_basis, bob_basis):
    if alice_basis == bob_basis:
        return bit
    return random.randint(0, 1)


def run_bb84(bit_num=32):

    alice_bits = [random.randint(0, 1) for _ in range(bit_num)]

    alice_bases = [random.randint(0, 1) for _ in range(bit_num)]

    bob_bases = [random.randint(0, 1) for _ in range(bit_num)]

    bob_bits = []

    for i in range(bit_num):

        measured = _measure_qubit(
            alice_bits[i],
            alice_bases[i],
            bob_bases[i]
        )

        # Wrong basis -> random measurement
        if alice_bases[i] != bob_bases[i]:
            measured = random.randint(0, 1)

        bob_bits.append(measured)

    alice_key = []
    bob_key = []

    for i in range(bit_num):

        if alice_bases[i] == bob_bases[i]:

            alice_key.append(str(alice_bits[i]))
            bob_key.append(str(bob_bits[i]))

    alice_key = "".join(alice_key)

    bob_key = "".join(bob_key)

    return {

        "alice_bits": alice_bits,

        "bob_bits": bob_bits,

        "alice_bases": alice_bases,

        "bob_bases": bob_bases,

        "alice_key": alice_key,

        "bob_key": bob_key,

        "shared_key": alice_key

    }
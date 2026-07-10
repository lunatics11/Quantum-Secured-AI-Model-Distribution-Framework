import random


def calculate_qber(alice_key, bob_key):
    """
    Calculate Quantum Bit Error Rate (QBER)
    """

    if len(alice_key) == 0:
        return 0.0

    errors = sum(a != b for a, b in zip(alice_key, bob_key))

    return errors / len(alice_key)


def detect_eve(qber, threshold=0.11):
    """
    Returns True if the QBER exceeds the security threshold.
    """

    return qber > threshold


def intercept_resend(key):
    """
    Simulate an intercept-resend attack.
    Approximately 25% of the sifted key bits are disturbed.
    """

    key = list(key)

    flips = max(1, len(key) // 4)

    positions = random.sample(range(len(key)), flips)

    for pos in positions:

        if key[pos] == "0":
            key[pos] = "1"
        else:
            key[pos] = "0"

    return "".join(key)


def mitm_attack(key):
    """
    Simulate a Man-in-the-Middle attack.
    About 50% of the key is corrupted.
    """

    key = list(key)

    flips = max(1, len(key) // 2)

    positions = random.sample(range(len(key)), flips)

    for pos in positions:

        if key[pos] == "0":
            key[pos] = "1"
        else:
            key[pos] = "0"

    return "".join(key)


def noisy_channel(key):
    """
    Simulate natural quantum channel noise.
    Around 10% of bits are flipped.
    """

    key = list(key)

    flips = max(1, len(key) // 10)

    positions = random.sample(range(len(key)), flips)

    for pos in positions:

        if key[pos] == "0":
            key[pos] = "1"
        else:
            key[pos] = "0"

    return "".join(key)
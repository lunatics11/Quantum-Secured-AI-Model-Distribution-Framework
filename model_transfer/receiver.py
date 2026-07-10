from crypto.aes_crypto import decrypt_bytes
import os


def receive_model(shared_key, output_filename):

    print("\n[Edge] Receiving encrypted model...")

    with open("storage/encrypted_model.bin", "rb") as f:
        encrypted = f.read()

    print("[Edge] Decrypting...")

    decrypted = decrypt_bytes(shared_key, encrypted)

    os.makedirs("storage", exist_ok=True)

    output_path = os.path.join(
        "storage",
        output_filename
    )

    with open(output_path, "wb") as f:
        f.write(decrypted)

    print("[Edge] Model stored successfully.")

    return output_path
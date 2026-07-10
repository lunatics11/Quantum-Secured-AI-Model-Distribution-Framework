from crypto.aes_crypto import encrypt_bytes
import os


def send_model(shared_key, model_path):

    print("\n[Cloud] Loading model...")

    with open(model_path, "rb") as f:
        model_data = f.read()

    print("[Cloud] Encrypting model...")

    encrypted = encrypt_bytes(shared_key, model_data)

    os.makedirs("storage", exist_ok=True)

    with open("storage/encrypted_model.bin", "wb") as f:
        f.write(encrypted)

    print("[Cloud] Encrypted model saved.")

    return {
        "model_name": os.path.basename(model_path),
        "model_size": len(model_data)
    }
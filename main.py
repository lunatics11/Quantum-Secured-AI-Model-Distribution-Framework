from qkd.bb84 import run_bb84

from model_transfer.sender import send_model
from model_transfer.receiver import receive_model

from crypto.hash_utils import sha256_file
from qkd.eve import (calculate_qber, detect_eve, attack_bob_key)
import streamlit as st


print("=" * 60)
print("Quantum-Secured AI Model Distribution Framework")
print("=" * 60)

# Generate BB84 Key
result = run_bb84(20)

shared_key = result["alice_key"]
SIMULATE_EVE = True

st.code(shared_key)

alice_key = result["alice_key"]
bob_key = result["bob_key"]

if SIMULATE_EVE:
    bob_key = attack_bob_key(bob_key)

qber = calculate_qber(alice_key, bob_key)

st.metric("QBER", round(qber, 3))

if detect_eve(qber):

    print("\n🚨 EAVESDROPPER DETECTED")
    st.error("Transfer Aborted")

    exit()

shared_key = alice_key

original_hash = sha256_file("models/model.pkl")

print("\nOriginal SHA256:")
print(original_hash)

# Cloud sends model
send_model(shared_key)

# Edge receives model
receive_model(shared_key)

# Verify integrity
received_hash = sha256_file("storage/decrypted_model.pkl")

print("\nReceived SHA256:")
print(received_hash)

print("\nIntegrity Check:")

if original_hash == received_hash:
    st.success("Integrity Verified")
else:
    print("FAIL")
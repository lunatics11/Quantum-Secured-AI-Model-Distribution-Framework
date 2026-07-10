import os
import sys

ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st

from app.styles import load_css
from app.dashboard import render_dashboard
from app.transfer import run_secure_transfer

from qkd.bb84 import run_bb84

from qkd.eve import (
    calculate_qber,
    detect_eve,
    intercept_resend,
    mitm_attack,
    noisy_channel,
)

# -----------------------------------------------------

st.set_page_config(

    page_title="QuantumSeal AI",

    page_icon="🛡️",

    layout="wide"

)

load_css()

# -----------------------------------------------------

with st.sidebar:

    st.title("QuantumSeal AI")

    st.markdown("---")

    attack = st.selectbox(

        "Attack Scenario",

        [

            "None",

            "Intercept-Resend",

            "Man-in-the-Middle",

            "Quantum Noise"

        ]

    )

    st.markdown("---")

    st.subheader("Security")

    st.write("BB84")

    st.write("AES-256")

    st.write("SHA-256")

    st.markdown("---")

    st.subheader("Model")

    uploaded_model = st.file_uploader(
        "Upload AI Model",
        type=[
            "pkl",
            "joblib",
            "pt",
            "pth",
            "onnx"
        ]
    )

    MODEL_PATH = "models/model.pkl"

    if uploaded_model is not None:

        os.makedirs("models", exist_ok=True)

        MODEL_PATH = os.path.join(
            "models",
            uploaded_model.name
        )

        with open(MODEL_PATH, "wb") as f:
            f.write(uploaded_model.getbuffer())

        st.success(uploaded_model.name)

        st.caption(
            f"{uploaded_model.size / 1024:.2f} KB"
        )

    else:

        st.caption("Else, Simply start to use demo model")

    st.markdown("---")

    start = st.button(

        "Start Secure Transfer",

        use_container_width=True

    )

# -----------------------------------------------------

render_dashboard()

# -----------------------------------------------------

if start:

    result = run_bb84(32)

    alice_key = result["alice_key"]

    bob_key = result["bob_key"]

    #################################################

    if attack == "Intercept-Resend":

        bob_key = intercept_resend(

            bob_key

        )

    elif attack == "Man-in-the-Middle":

        bob_key = mitm_attack(

            bob_key

        )

    elif attack == "Quantum Noise":

        bob_key = noisy_channel(

            bob_key

        )

    #################################################

    qber = calculate_qber(

        alice_key,

        bob_key

    )

    #################################################

    if detect_eve(qber):

        st.error(

            f"""

Attack Detected

QBER : {qber:.3f}

Transfer Blocked

"""

        )

        st.stop()

    #################################################

    if uploaded_model is None:
        st.warning("Please upload an AI model to start the secure transfer.")
        st.stop()

    run_secure_transfer(

        alice_key,

        qber,

        attack,

        MODEL_PATH

    )
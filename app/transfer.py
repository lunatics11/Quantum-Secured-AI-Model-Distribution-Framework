import os
import time
import streamlit as st
from pathlib import Path

from model_transfer.sender import send_model
from model_transfer.receiver import receive_model
from crypto.hash_utils import sha256_file

from app.components import (
    network_topology,
    transfer_report,
    activity_log
)


def run_secure_transfer(alice_key, qber, attack, model_path):

    network_placeholder = st.empty()

    progress = st.progress(0)

    status = st.empty()

    logs_placeholder = st.empty()

    logs = []

    timeline = [

        ("Generating BB84 Quantum Key", 10),

        ("Deriving AES Session Key", 25),

        ("Encrypting AI Model", 45),

        ("Uploading Encrypted Model", 65),

        ("Receiving Model", 80),

        ("Decrypting Model", 90),

        ("Verifying SHA-256 Integrity", 100)

    ]

    for step, percent in timeline:

        network_placeholder.empty()

        with network_placeholder.container():

            network_topology("TRANSFER")

        status.info(step)

        logs.append(step)

        with logs_placeholder.container():

            activity_log(logs)

        progress.progress(percent)

        time.sleep(0.45)

    model_info = send_model(
        alice_key,
        model_path
    )

    output_path = receive_model(
        alice_key,
        model_info["model_name"]
    )

    original_hash = sha256_file(model_path)

    received_hash = sha256_file(output_path)

    network_placeholder.empty()

    with network_placeholder.container():

        network_topology("SUCCESS")

    st.success("Secure AI Model Successfully Delivered")

    ####################################################
    # MODEL INFORMATION
    ####################################################

    model_name = Path(model_path).name

    model_type = Path(model_path).suffix.upper()

    model_size = os.path.getsize(model_path)

    model_hash = original_hash[:16] + "..."

    framework_map = {
        ".pt": "PyTorch",
        ".pth": "PyTorch",
        ".onnx": "ONNX",
        ".pkl": "Scikit-Learn",
        ".joblib": "Scikit-Learn",
    }

    framework = framework_map.get(
        Path(model_path).suffix.lower(),
        "Unknown"
    )

    st.markdown("---")

    st.subheader("Model Information")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Model Name",
            model_name
        )

        st.metric(
            "Framework",
            framework
        )

    with c2:

        st.metric(
            "File Type",
            model_type
        )

        st.metric(
            "File Size",
            f"{model_size / (1024*1024):.2f} MB"
        )

    with c3:

        st.metric(
            "Transfer",
            "SUCCESS"
        )

        st.metric(
            "Integrity",
            "PASS" if original_hash == received_hash else "FAIL"
        )

    st.markdown("---")

    transfer_report(

        qber=qber,

        key=len(alice_key),

        attack=attack,

        integrity="PASS" if original_hash == received_hash else "FAIL"

    )

    st.markdown("---")

    st.subheader("Transferred Model")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Model Name",
            model_info["model_name"]
        )

        st.metric(
            "File Size",
            f"{model_info['model_size'] / 1024:.2f} KB"
        )

    with c2:

        st.metric(
            "QBER",
            f"{qber:.3f}"
        )

        st.metric(
            "Key Length",
            len(alice_key)
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Original SHA-256")

        st.code(original_hash)

    with col2:

        st.subheader("Received SHA-256")

        st.code(received_hash)

    if original_hash == received_hash:

        st.success("✔ Integrity Verification Passed")

    else:

        st.error("✖ Integrity Verification Failed")

    with st.expander("Quantum Shared Key"):

        st.code(alice_key)

    with st.expander("Transfer Timeline"):

        activity_log(logs)
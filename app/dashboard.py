import streamlit as st

from app.components import (
    status_cards,
    network_topology,
)


def render_dashboard():

    st.markdown(
        """
<div class="title">

QShield AI

</div>

<div class="subtitle">

Quantum-Secured AI Model Distribution Platform

</div>

""",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    status_cards()

    st.markdown("<br>", unsafe_allow_html=True)

    network_topology("READY")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
### Overview

This platform demonstrates secure distribution of AI models
using BB84 Quantum Key Distribution.

The generated quantum key is used for AES encryption of the
model before transmission.

After delivery, SHA-256 integrity verification ensures the
model has not been modified.
"""
    )
import streamlit as st

STATUS_COLORS = {
    "READY": "#3B82F6",
    "TRANSFER": "#F59E0B",
    "SUCCESS": "#22C55E",
    "ATTACK": "#EF4444",
}


def status_badge(status):

    status = status.upper()

    mapping = {
        "READY": "badge-ready",
        "TRANSFER": "badge-transfer",
        "SUCCESS": "badge-success",
        "ATTACK": "badge-attack",
    }

    css = mapping.get(status, "badge-ready")

    return f"""
<span class="status-badge {css}">
{status}
</span>
"""


########################################################


def status_card(title, value, color):

    st.markdown(
        f"""
<div class="status-card fade-in">

<div class="card-title">

{title}

</div>

<div
style="
font-size:32px;
font-weight:700;
color:white;
margin-top:8px;
">

{value}

</div>

<div
style="
margin-top:18px;
height:5px;
border-radius:50px;
background:{color};
box-shadow:0 0 18px {color};
">

</div>

</div>
""",
        unsafe_allow_html=True,
    )


########################################################


def status_cards():

    c1, c2, c3 = st.columns(3)

    with c1:

        status_card(

            "Cloud Server",

            "ONLINE",

            "#22C55E"

        )

    with c2:

        status_card(

            "QKD Gateway",

            "ACTIVE",

            "#3B82F6"

        )

    with c3:

        status_card(

            "Edge AI",

            "READY",

            "#F59E0B"

        )


########################################################


def network_topology(status="READY"):

    color = STATUS_COLORS.get(status, "#3B82F6")

    badge = status_badge(status)

    st.markdown(
        f"""

<div class="network-card fade-in">

<div
style="
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:30px;
">

<div>

<div class="network-title">

Quantum Network Topology

</div>

<div
style="
color:#94A3B8;
">

Secure AI Model Distribution Channel

</div>

</div>

<div>

{badge}

</div>

</div>

<div class="network-row">

<div class="node">

<div
style="
font-size:13px;
color:#94A3B8;
">

SOURCE

</div>

<div
style="
margin-top:6px;
font-size:18px;
">

Cloud Server

</div>

</div>

<div class="line">

<div class="dot"></div>

</div>
<div class="node">

<div
style="
font-size:13px;
color:#94A3B8;
">

QKD

</div>

<div
style="
margin-top:6px;
font-size:18px;
">

Gateway

</div>

</div>

<div class="line">

<div class="dot"></div>

</div>

<div class="node">

<div
style="
font-size:13px;
color:#94A3B8;
">

DESTINATION

</div>

<div
style="
margin-top:6px;
font-size:18px;
">

Edge Device

</div>

</div>

</div>

<div
style="
margin-top:35px;
display:flex;
justify-content:space-around;
">

<div>

<div
style="
color:#94A3B8;
font-size:13px;
">

Protocol

</div>

<div
style="
margin-top:6px;
font-size:18px;
font-weight:700;
">

BB84

</div>

</div>

<div>

<div
style="
color:#94A3B8;
font-size:13px;
">

Encryption

</div>

<div
style="
margin-top:6px;
font-size:18px;
font-weight:700;
">

AES-256

</div>

</div>

<div>

<div
style="
color:#94A3B8;
font-size:13px;
">

Integrity

</div>

<div
style="
margin-top:6px;
font-size:18px;
font-weight:700;
">

SHA-256

</div>

</div>

</div>

</div>

""",
        unsafe_allow_html=True,
    )


########################################################


def transfer_report(
    qber,
    key,
    attack,
    integrity,
):

    c1, c2 = st.columns(2)

    with c1:

        status_card(
            "QBER",
            f"{qber:.3f}",
            "#22C55E",
        )

        st.markdown("<br>", unsafe_allow_html=True)

        status_card(
            "Attack",
            attack,
            "#EF4444" if attack != "None" else "#22C55E",
        )

    with c2:

        status_card(
            "Key Length",
            str(key),
            "#3B82F6",
        )

        st.markdown("<br>", unsafe_allow_html=True)

        status_card(
            "Integrity",
            integrity,
            "#22C55E",
        )
########################################################


def activity_log(logs):

    html = ""

    for log in logs:

        html += f"""
<div class="log-entry">

{log}

</div>
"""

    st.markdown(
        f"""

<div class="log-card fade-in">

<div
style="
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:15px;
">

<div
style="
font-size:22px;
font-weight:700;
">

Transfer Timeline

</div>

<div>

{status_badge("SUCCESS")}

</div>

</div>

<div class="timeline">

{html}

</div>

</div>

""",
        unsafe_allow_html=True,
    )


########################################################


def security_summary(
    qber,
    attack,
    integrity,
):

    st.markdown(
        f"""

<div class="network-card fade-in">

<div
style="
font-size:24px;
font-weight:700;
margin-bottom:20px;
">

Security Summary

</div>

<table
style="
width:100%;
border-collapse:collapse;
">

<tr>

<td style="padding:12px;color:#94A3B8;">

Protocol

</td>

<td
style="
padding:12px;
font-weight:700;
">

BB84 Quantum Key Distribution

</td>

</tr>

<tr>

<td style="padding:12px;color:#94A3B8;">

Encryption

</td>

<td
style="
padding:12px;
font-weight:700;
">

AES-256

</td>

</tr>

<tr>

<td style="padding:12px;color:#94A3B8;">

Integrity

</td>

<td
style="
padding:12px;
font-weight:700;
color:#22C55E;
">

{integrity}

</td>

</tr>

<tr>

<td style="padding:12px;color:#94A3B8;">

Attack

</td>

<td
style="
padding:12px;
font-weight:700;
">

{attack}

</td>

</tr>

<tr>

<td style="padding:12px;color:#94A3B8;">

QBER

</td>

<td
style="
padding:12px;
font-weight:700;
">

{qber:.3f}

</td>

</tr>

</table>

</div>

""",
        unsafe_allow_html=True,
    )
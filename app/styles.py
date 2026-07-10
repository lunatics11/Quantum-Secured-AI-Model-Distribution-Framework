import streamlit as st


def load_css():

    st.markdown("""
<style>

/* ==========================
   GLOBAL
========================== */

:root{

    --bg:#0B1220;
    --panel:#111827;
    --panel2:#1F2937;

    --text:#F3F4F6;
    --muted:#94A3B8;

    --blue:#3B82F6;
    --green:#22C55E;
    --red:#EF4444;
    --orange:#F59E0B;

}

html,
body,
[class*="css"]{

    background:var(--bg);

    color:var(--text);

    font-family:Inter,sans-serif;

}

/* ==========================
   STREAMLIT
========================== */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}

header{
    background: transparent;
}

.stApp{

    background:linear-gradient(
        180deg,
        #09101C,
        #0B1220
    );

}

/* ==========================
   SIDEBAR
========================== */

section[data-testid="stSidebar"]{

    background:#0F172A;

    border-right:1px solid #1F2937;

}

section[data-testid="stSidebar"] h1{

    color:white;

    font-weight:700;

}

section[data-testid="stSidebar"]{

    padding-top:20px;

}

/* ==========================
   BUTTON
========================== */

.stButton>button{

    width:100%;

    height:48px;

    border:none;

    border-radius:12px;

    background:linear-gradient(
        90deg,
        #2563EB,
        #3B82F6
    );

    color:white;

    font-weight:700;

    transition:.3s;

}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:
        0 0 20px
        rgba(59,130,246,.45);

}

/* ==========================
   TITLE
========================== */

.title{

    font-size:42px;

    font-weight:800;

    color:white;

    letter-spacing:.5px;

}

.subtitle{

    color:#94A3B8;

    font-size:17px;

    margin-top:5px;

    margin-bottom:30px;

}

/* ==========================
   STATUS CARD
========================== */

.status-card{

    background:rgba(17,24,39,.82);

    backdrop-filter:blur(16px);

    border-radius:18px;

    padding:22px;

    border:1px solid #1F2937;

    transition:.25s;

    box-shadow:

        0 0 20px

        rgba(0,0,0,.30);

}

.status-card:hover{

    transform:translateY(-4px);

    border-color:#2563EB;

    box-shadow:

        0 0 25px

        rgba(37,99,235,.25);

}

.card-title{

    color:#94A3B8;

    font-size:14px;

}

.card-status{

    margin-top:10px;

    color:white;

    font-size:28px;

    font-weight:700;

}
/* ==========================
   NETWORK CARD
========================== */

.network-card{

    background:rgba(17,24,39,.88);

    backdrop-filter:blur(20px);

    border-radius:20px;

    border:1px solid #1F2937;

    padding:28px;

    margin-top:10px;

    margin-bottom:20px;

    box-shadow:

        0 0 30px rgba(0,0,0,.28);

}

.network-title{

    font-size:24px;

    font-weight:700;

    margin-bottom:28px;

}

.network-row{

    display:flex;

    align-items:center;

    justify-content:center;

}

/* ==========================
   NODES
========================== */

.node{

    width:170px;

    background:#111827;

    border:2px solid #2563EB;

    border-radius:16px;

    padding:18px;

    color:white;

    text-align:center;

    font-weight:700;

    letter-spacing:.5px;

    transition:.3s;

}

.node:hover{

    transform:scale(1.04);

    box-shadow:

        0 0 18px rgba(37,99,235,.45);

}

/* ==========================
   NETWORK LINE
========================== */

.line{

    position:relative;

    flex:1;

    height:6px;

    background:#233045;

    margin:0 12px;

    border-radius:999px;

    overflow:hidden;

}

/* ==========================
   MOVING PACKET
========================== */

.dot{

    width:16px;

    height:16px;

    position:absolute;

    top:-5px;

    left:0;

    border-radius:50%;

    background:#3B82F6;

    box-shadow:

        0 0 18px #3B82F6,

        0 0 35px #3B82F6;

    animation:

        packetMove

        2.2s

        linear

        infinite;

}

@keyframes packetMove{

0%{

left:-2%;

}

100%{

left:100%;

}

}

/* ==========================
   METRIC
========================== */

[data-testid="metric-container"]{

    background:#111827;

    border:1px solid #1F2937;

    border-radius:18px;

    padding:18px;

    box-shadow:

        0 0 20px rgba(0,0,0,.25);

}

[data-testid="metric-container"]:hover{

    border-color:#2563EB;

}
/* ==========================
   PROGRESS BAR
========================== */

.stProgress{

    margin-top:15px;

    margin-bottom:20px;

}

.stProgress > div{

    background:#1F2937 !important;

    border-radius:999px;

    overflow:hidden;

    height:14px;

}

.stProgress > div > div{

    background:linear-gradient(
        90deg,
        #2563EB,
        #3B82F6,
        #60A5FA
    ) !important;

    border-radius:999px;

    animation:progressGlow 2s infinite alternate;

}

@keyframes progressGlow{

from{

filter:brightness(100%);

}

to{

filter:brightness(145%);

}

}

/* ==========================
   CODE BLOCK
========================== */

pre{

    border-radius:16px !important;

    border:1px solid #1F2937 !important;

    background:#0F172A !important;

    color:#E5E7EB !important;

    padding:18px !important;

}

/* ==========================
   EXPANDER
========================== */

.streamlit-expanderHeader{

    background:#111827;

    border-radius:12px;

    font-weight:700;

    color:white;

    border:1px solid #1F2937;

}

.streamlit-expanderContent{

    border:1px solid #1F2937;

    border-top:none;

}

/* ==========================
   ALERTS
========================== */

div[data-baseweb="notification"]{

    border-radius:14px;

    border:none;

}

/* ==========================
   ACTIVITY LOG
========================== */

.log-card{

    background:#111827;

    border:1px solid #1F2937;

    border-radius:18px;

    padding:20px;

    margin-top:15px;

}

.log-entry{

    border-bottom:1px solid #1F2937;

    padding:10px;

    color:#E5E7EB;

    transition:.2s;

}

.log-entry:last-child{

    border-bottom:none;

}

.log-entry:hover{

    background:#172554;

    border-radius:8px;

}

/* ==========================
   TIMELINE
========================== */

.timeline{

    margin-top:20px;

}

.timeline-item{

    display:flex;

    align-items:center;

    gap:14px;

    margin-bottom:14px;

}

.timeline-dot{

    width:14px;

    height:14px;

    border-radius:50%;

    background:#22C55E;

    box-shadow:

        0 0 12px #22C55E;

}

.timeline-text{

    color:white;

    font-size:15px;

}
/* ==========================
   STATUS BADGE
========================== */

.status-badge{

    display:inline-block;

    padding:8px 18px;

    border-radius:999px;

    font-size:13px;

    font-weight:700;

    color:white;

    animation:pulseGlow 2s infinite;

}

.badge-ready{

    background:#2563EB;

}

.badge-transfer{

    background:#F59E0B;

}

.badge-success{

    background:#22C55E;

}

.badge-attack{

    background:#EF4444;

}

@keyframes pulseGlow{

0%{

transform:scale(1);

filter:brightness(100%);

}

50%{

transform:scale(1.05);

filter:brightness(130%);

}

100%{

transform:scale(1);

filter:brightness(100%);

}

}

/* ==========================
   FADE ANIMATION
========================== */

.fade-in{

    animation:fadeIn .8s ease;

}

@keyframes fadeIn{

from{

opacity:0;

transform:translateY(10px);

}

to{

opacity:1;

transform:translateY(0);

}

}

/* ==========================
   SCROLLBAR
========================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#111827;

}

::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:999px;

}

::-webkit-scrollbar-thumb:hover{

    background:#475569;

}

/* ==========================
   FOOTER
========================== */

.footer{

    margin-top:40px;

    padding:18px;

    text-align:center;

    color:#94A3B8;

    font-size:13px;

    border-top:1px solid #1F2937;

}

/* ==========================
   RESPONSIVE
========================== */

@media(max-width:1100px){

.network-row{

flex-direction:column;

gap:25px;

}

.line{

width:6px;

height:80px;

}

.dot{

animation:packetMoveVertical 2s linear infinite;

top:0;

left:-5px;

}

@keyframes packetMoveVertical{

0%{

top:-2%;

}

100%{

top:100%;

}

}

.node{

width:100%;

}

.title{

font-size:30px;

}

.subtitle{

font-size:15px;

}

}

</style>
""", unsafe_allow_html=True)
"""Nikaah invitation of Fehmina & Alimuzzama, served as a full-screen Streamlit page.

The invitation itself (envelope animation, card, details) lives in invite.html.
This app hides Streamlit's own header, menu and padding so guests only see the card.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Fehmina & Alimuzzama",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], [data-testid="stSidebar"] { display: none !important; }
      html, body, .stApp { background: #efe9dc; }
      [data-testid="stAppViewContainer"], [data-testid="stMain"],
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;
      }
      [data-testid="stMain"] { overflow: hidden !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"]:has(> [data-testid="stMarkdown"] style) { display: none !important; }
      iframe {
        display: block; border: 0;
        width: 100% !important;
        height: 100vh !important;
        height: 100dvh !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

invite = (Path(__file__).parent / "invite.html").read_text(encoding="utf-8")
components.html(invite, height=900, scrolling=True)

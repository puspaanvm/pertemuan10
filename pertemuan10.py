import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")

kamus_ticker = {
    "GOOGL": 'Google',
    'AAPL': 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD': "McDonald's Corp",
    'META': "Meta Platforms Inc",
    'TLKM.JK': "Telkom Indonesia (Persero) Tbk PT",
    'BBNI': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nestle SA',
    'BBCA.JK': 'Bank Central Asia Tbk PT'

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted( kamus_ticker.keys() )
)
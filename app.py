import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="CAN-CCHD Agent",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

from can_cchd.ui.main_console import render_sidebar, render_main_console

def main():
    render_sidebar()
    render_main_console()

if __name__ == "__main__":
    main()

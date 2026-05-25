import streamlit as st
import time
import pygetwindow as gw

st.title("🧠 Local AI Productivity Tracker")

def get_active_window():

    try:

        window = gw.getActiveWindow()

        if window:
            return window.title

        return "Unknown"

    except:

        return "Unknown"

if st.button("🚀 Start Tracking"):

    for i in range(20):

        active_app = get_active_window()

        st.write(f"Current App: {active_app}")

        time.sleep(1)
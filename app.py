
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page configuration
st.set_page_config(page_title="F1 Track Analyzer", layout="wide")

# Define navigation options
tabs = {
    "Dashboard": "dashboard",
    "Tires": "tires",
    "Graphs": "graphs"
}

# Sidebar navigation
selected_tab = st.sidebar.radio("Navigate", list(tabs.keys()))

# Circuit image mapping
circuit_images = {
    "Abu Dhabi": "abu_dhabi.png",
    "Silverstone": "silverstone.png",
    "Monaco": "monaco.png"
}

def show_dashboard():
    st.title("F1 Track Analyzer")
    st.markdown("## Select Circuit:")
    circuit = st.selectbox("Choose a circuit:", list(circuit_images.keys()))

    st.image(
        os.path.join("images", circuit_images[circuit]),
        width=700,
        caption=f"{circuit} Circuit Map"
    )

    st.markdown("---")
    st.markdown("## Upload your CSV telemetry data:")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")

    if uploaded_file is not None:
        st.success("CSV uploaded successfully!")
        if st.button("Analyze"):
            df = pd.read_csv(uploaded_file)
            st.markdown("### Here's a quick look at your data:")
            st.dataframe(df, use_container_width=True)

def show_tires():
    st.title("Tire Analysis")
    st.markdown("This section will display tire degradation over laps.")
    st.markdown("Coming soon...")

def show_graphs():
    st.title("Telemetry Graphs")
    st.markdown("Upload CSV to visualize lap telemetry.")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        if 'LapTime' in df.columns and 'LapNumber' in df.columns:
            st.markdown("### Lap Times Over Laps")
            fig, ax = plt.subplots()
            ax.plot(df['LapNumber'], df['LapTime'], marker='o')
            ax.set_xlabel("Lap Number")
            ax.set_ylabel("Lap Time")
            ax.set_title("Lap Time per Lap")
            st.pyplot(fig)
        else:
            st.warning("CSV must contain 'LapNumber' and 'LapTime' columns.")

# Route based on tab
if tabs[selected_tab] == "dashboard":
    show_dashboard()
elif tabs[selected_tab] == "tires":
    show_tires()
elif tabs[selected_tab] == "graphs":
    show_graphs()

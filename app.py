import streamlit as st

st.set_page_config(
    page_title="HealthGuardian AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 HealthGuardian AI")
st.subheader("Your Personal AI Healthcare Assistant")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a Module",
    [
        "🏠 Home",
        "👤 Patient Registration",
        "📄 Prescription Upload",
        "💊 Medicine Manager",
        "❤️ Wellness Check",
        "🤖 AI Assistant",
        "🚨 Emergency Detection",
        "📅 Appointment Booking"
    ]
)

if page == "🏠 Home":
    st.header("Welcome to HealthGuardian AI")

    st.write("""
    This application helps patients manage their healthcare using Artificial Intelligence.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.info("👤 Register Patient")
        st.info("📄 Upload Prescription")
        st.info("💊 Medicine Management")
        st.info("❤️ Daily Wellness")

    with col2:
        st.info("🤖 AI Health Assistant")
        st.info("🚨 Emergency Detection")
        st.info("📅 Appointment Booking")
        st.info("👨‍⚕️ Caregiver Notifications")

elif page == "👤 Patient Registration":
    st.header("Patient Registration")
    st.write("This module will be connected in the next step.")

elif page == "📄 Prescription Upload":
    st.header("Prescription Upload")
    st.write("This module will be connected in the next step.")

elif page == "💊 Medicine Manager":
    st.header("Medicine Manager")
    st.write("This module will be connected in the next step.")

elif page == "❤️ Wellness Check":
    st.header("Daily Wellness Check")
    st.write("This module will be connected in the next step.")

elif page == "🤖 AI Assistant":
    st.header("AI Health Assistant")
    st.write("This module will be connected in the next step.")

elif page == "🚨 Emergency Detection":
    st.header("Emergency Detection")
    st.write("This module will be connected in the next step.")

elif page == "📅 Appointment Booking":
    st.header("Appointment Booking")
    st.write("This module will be connected in the next step.")

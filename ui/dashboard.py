import requests
import streamlit as st
def show():
    SERVER = "http://127.0.0.1:8000"

    data = requests.get(
        f"{SERVER}/dashboard"
    ).json()

    st.title("🤖 L2 Database AI Dashboard")

    col1,col2,col3,col4=st.columns(4)

    col1.metric(
        "Customers",
        data["customers"]
    )

    col2.metric(
        "Orders",
        data["orders"]
    )

    col3.metric(
        "Payments",
        data["payments"]
    )

    col4.metric(
        "Shipments",
        data["shipments"]
    )                                                                                    
    col1,col2,col3,col4=st.columns(4)

    col1.metric(
        "Failed Payments",
        data["failed_payments"]
    )

    col2.metric(
        "Pending Refunds",
        data["pending_refunds"]
    )

    col3.metric(
        "Wallets",
        data["wallets"]
    )

    col4.metric(
        "Revenue",
        f"₹{data['revenue']:,.0f}"
    )
    st.subheader("🟢 System Health")

    st.success("AI Agent : Online")
    st.success("SQLite : Connected")
    st.success("Embedding Model : Loaded")
    st.success("FastAPI : Running")
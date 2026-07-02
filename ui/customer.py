import streamlit as st
import requests
import pandas as pd

def show():
    SERVER_URL = "http://127.0.0.1:8000"

    st.title("👥 Customer Management")
    st.caption("L2 Database Support Portal")

    # -----------------------------
    # 1. Load Customers
    # -----------------------------
    try:
        response = requests.get(f"{SERVER_URL}/customers")
        customers = response.json()
    except Exception:
        st.error("Unable to connect to backend.")
        st.stop()

    # -----------------------------
    # 2. Sidebar Search
    # -----------------------------
    search = ""  # You can replace this with st.sidebar.text_input("Search")
    filtered = customers

    if search:
        filtered = [
            c for c in customers
            if search.lower() in c["customer_name"].lower()
            or search.lower() in c["email"].lower()
        ]

    customer_names = [f'{c["customer_id"]} - {c["customer_name"]}' for c in filtered]
    selected = st.sidebar.selectbox("Customers", customer_names)
    customer_id = int(selected.split(" - ")[0])

    # -----------------------------
    # 3. Fetch Data
    # -----------------------------
    customer = requests.get(f"{SERVER_URL}/customers/{customer_id}").json()
    summary = requests.get(f"{SERVER_URL}/customers/{customer_id}/summary").json()
    accounts = requests.get(f"{SERVER_URL}/customers/{customer_id}/accounts").json()
    orders = requests.get(f"{SERVER_URL}/customers/{customer_id}/orders").json()
    wallet = requests.get(f"{SERVER_URL}/customers/{customer_id}/wallet").json()
    addresses = requests.get(f"{SERVER_URL}/customers/{customer_id}/addresses").json()

    # -----------------------------
    # 4. Header & Summary
    # -----------------------------
    left, right = st.columns([5, 1])
    with left:
        st.header(customer["customer_name"])
        st.caption(customer["email"])
    with right:
        if customer["status"] == "ACTIVE":
            st.success("ACTIVE")
        else:
            st.error(customer["status"])

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Orders", summary["orders"])
    c2.metric("Accounts", summary["accounts"])
    c3.metric("Addresses", summary["addresses"])
    c4.metric("Wallet", f"₹{summary['wallet_balance']}")

    st.divider()

    # -----------------------------
    # 5. Detail Tabs
    # -----------------------------
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["👤 Profile", "🏦 Accounts", "📦 Orders", "💳 Wallet", "📍 Addresses"]
    )

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Customer ID", customer["customer_id"], disabled=True)
            st.text_input("Name", customer["customer_name"], disabled=True)
            st.text_input("Email", customer["email"], disabled=True)
        with col2:
            st.text_input("Phone", customer["phone"], disabled=True)
            st.text_input("Status", customer["status"], disabled=True)
            st.text_input("Created", customer["created_at"], disabled=True)

    with tab2:
        st.subheader("Customer Accounts")
        st.dataframe(pd.DataFrame(accounts), use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("Orders")
        st.dataframe(pd.DataFrame(orders), use_container_width=True, hide_index=True)

    with tab4:
        st.metric("Wallet Balance", f"₹{wallet['wallet_balance']}")
        st.write("Last Updated:", wallet["last_updated"])

    with tab5:
        st.dataframe(pd.DataFrame(addresses), use_container_width=True, hide_index=True)

    st.divider()

    # -----------------------------
    # 6. AI Investigation
    # -----------------------------
    st.subheader("🤖 AI Investigation")
    if st.button("Investigate Customer", use_container_width=True):
        with st.spinner("AI is investigating..."):
            result = requests.post(
                f"{SERVER_URL}/chat",
                json={"query": f"Investigate customer {customer_id}"}
            )
            st.success(result.json()["answer"])
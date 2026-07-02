import streamlit as st
import pandas as pd
import requests
def show():


    API_URL = "http://localhost:8000"

    st.title("💸 Transaction Management")
    st.caption("Investigate payment gateway transactions")

    # --------------------------------------------------------
    # Filters
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        transaction_id = st.text_input("🔍 Transaction ID")

    with col2:
        payment_id = st.text_input("💳 Payment ID")

    with col3:
        status = st.selectbox(
            "Transaction Status",
            ["All", "SUCCESS", "FAILED", "PENDING"]
        )

    with col4:
        failure = st.text_input("Failure Reason")

    st.divider()

    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Transactions", 200)
    m2.metric("Successful", 170)
    m3.metric("Failed", 20)
    m4.metric("Pending", 10)

    st.divider()

    # --------------------------------------------------------
    # Table
    # --------------------------------------------------------

    response = requests.get(f"{API_URL}/transactions")

    if response.status_code == 200:

        df = pd.DataFrame(response.json())

        if transaction_id:
            df = df[df["transaction_id"].astype(str).str.contains(transaction_id)]

        if payment_id:
            df = df[df["payment_id"].astype(str).str.contains(payment_id)]

        if status != "All":
            df = df[df["transaction_status"] == status]

        if failure:
            df = df[
                df["failure_reason"]
                .fillna("")
                .str.contains(failure, case=False)
            ]

        st.dataframe(df, use_container_width=True)

        st.divider()

        selected = st.selectbox(
            "Select Transaction",
            df["transaction_id"]
        )

        detail = requests.get(
            f"{API_URL}/transactions/{selected}"
        ).json()

        tab1, tab2, tab3 = st.tabs([
            "📄 Details",
            "🏦 References",
            "🤖 AI Investigation"
        ])

        with tab1:

            st.write(f"**Transaction ID:** {detail['transaction_id']}")
            st.write(f"**Payment ID:** {detail['payment_id']}")
            st.write(f"**Status:** {detail['transaction_status']}")
            st.write(f"**Failure Reason:** {detail['failure_reason']}")
            st.write(f"**Time:** {detail['transaction_time']}")

        with tab2:

            st.write(f"**Bank Reference:** {detail['bank_reference']}")
            st.write(f"**Gateway Reference:** {detail['gateway_reference']}")

        with tab3:

            if st.button("Investigate Transaction"):
                st.success(
                    "AI investigation will appear here."
                )

    else:

        st.error("Unable to load transactions.")
import streamlit as st
import pandas as pd
import requests
def show():

    API_URL = "http://localhost:8000"

    st.title("💰 Refund Management")
    st.caption("Track and investigate customer refunds")

    # --------------------------------------------------------
    # Filters
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        refund_id = st.text_input("Refund ID")

    with col2:
        transaction_id = st.text_input("Transaction ID")

    with col3:
        status = st.selectbox(
            "Refund Status",
            [
                "All",
                "INITIATED",
                "COMPLETED",
                "FAILED"
            ]
        )

    st.divider()

    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------

    m1, m2, m3 = st.columns(3)

    m1.metric("Refunds", 50)
    m2.metric("Completed", 40)
    m3.metric("Pending", 10)

    st.divider()

    # --------------------------------------------------------
    # Refund Table
    # --------------------------------------------------------

    response = requests.get(f"{API_URL}/refunds")

    if response.status_code == 200:

        df = pd.DataFrame(response.json())

        if refund_id:
            df = df[df["refund_id"].astype(str).str.contains(refund_id)]

        if transaction_id:
            df = df[
                df["transaction_id"]
                .astype(str)
                .str.contains(transaction_id)
            ]

        if status != "All":
            df = df[df["refund_status"] == status]

        st.dataframe(df, use_container_width=True)

        st.divider()

        selected = st.selectbox(
            "Select Refund",
            df["refund_id"]
        )

        detail = requests.get(
            f"{API_URL}/refunds/{selected}"
        ).json()

        tab1, tab2 = st.tabs([
            "📄 Refund Details",
            "🤖 AI Investigation"
        ])

        with tab1:

            st.write(f"**Refund ID:** {detail['refund_id']}")
            st.write(f"**Transaction ID:** {detail['transaction_id']}")
            st.write(f"**Amount:** ₹{detail['refund_amount']}")
            st.write(f"**Status:** {detail['refund_status']}")
            st.write(f"**Refund Date:** {detail['refund_date']}")

        with tab2:

            if st.button("Investigate Refund"):

                st.success(
                    "AI investigation will appear here."
                )

    else:

        st.error("Unable to load refunds.")
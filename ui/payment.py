import streamlit as st
import pandas as pd
import requests
def show():


    API_URL = "http://localhost:8000"

    st.title("💳 Payment Management")
    st.caption("Monitor and investigate customer payments")

    # ==========================================================
    # Filters
    # ==========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        payment_id = st.text_input("🔍 Payment ID")

    with col2:
        order_id = st.text_input("📦 Order ID")

    with col3:
        status = st.selectbox(
            "Payment Status",
            [
                "All",
                "SUCCESS",
                "FAILED",
                "PENDING"
            ]
        )

    with col4:
        mode = st.selectbox(
            "Payment Mode",
            [
                "All",
                "UPI",
                "Credit Card",
                "Debit Card",
                "Net Banking"
            ]
        )

    st.divider()

    # ==========================================================
    # Summary
    # ==========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total Payments", 200)

    with c2:
        st.metric("Successful", 168)

    with c3:
        st.metric("Failed", 21)

    with c4:
        st.metric("Pending", 11)

    st.divider()

    # ==========================================================
    # Load Payments
    # ==========================================================

    response = requests.get(f"{API_URL}/payments")

    if response.status_code == 200:

        payments = response.json()

        df = pd.DataFrame(payments)

        if payment_id:
            df = df[df["payment_id"].astype(str).str.contains(payment_id)]

        if order_id:
            df = df[df["order_id"].astype(str).str.contains(order_id)]

        if status != "All":
            df = df[df["payment_status"] == status]

        if mode != "All":
            df = df[df["payment_mode"] == mode]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("Payment Details")

        payment = st.selectbox(
            "Select Payment",
            df["payment_id"]
        )

        if payment:

            detail = requests.get(
                f"{API_URL}/payments/{payment}"
            ).json()

            col1, col2 = st.columns([2, 1])

            with col1:

                st.info("### Payment Information")

                st.write(f"**Payment ID:** {detail['payment_id']}")
                st.write(f"**Order ID:** {detail['order_id']}")
                st.write(f"**Amount:** ₹{detail['amount']}")
                st.write(f"**Mode:** {detail['payment_mode']}")
                st.write(f"**Status:** {detail['payment_status']}")
                st.write(f"**Time:** {detail['payment_time']}")

            with col2:

                st.info("### Actions")

                st.button(
                    "📦 View Order",
                    use_container_width=True
                )

                st.button(
                    "🏦 View Transaction",
                    use_container_width=True
                )

                st.button(
                    "🤖 AI Investigation",
                    use_container_width=True
                )

    else:
        st.error("Unable to load payments.")
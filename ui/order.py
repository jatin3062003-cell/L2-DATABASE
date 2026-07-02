import streamlit as st
import pandas as pd
import requests

def show():


    API_URL = "http://localhost:8000"

    st.title("📦 Order Management")
    st.caption("Monitor and investigate customer orders")

    # ==========================================================
    # Filters
    # ==========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        order_id = st.text_input(
            "🔍 Order ID"
        )

    with col2:
        customer = st.text_input(
            "👤 Customer ID"
        )

    with col3:
        status = st.selectbox(
            "Order Status",
            [
                "All",
                "CREATED",
                "PROCESSING",
                "SHIPPED",
                "DELIVERED",
                "CANCELLED"
            ]
        )

    with col4:
        payment = st.selectbox(
            "Payment Status",
            [
                "All",
                "SUCCESS",
                "FAILED",
                "PENDING"
            ]
        )

    st.divider()

    # ==========================================================
    # Summary
    # ==========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total Orders", 200)

    with c2:
        st.metric("Delivered", 132)

    with c3:
        st.metric("Processing", 42)

    with c4:
        st.metric("Cancelled", 26)

    st.divider()

    # ==========================================================
    # Orders Table
    # ==========================================================

    response = requests.get(f"{API_URL}/orders")

    if response.status_code == 200:

        orders = response.json()

        df = pd.DataFrame(orders)

        if order_id:
            df = df[
                df["order_id"].astype(str).str.contains(order_id)
            ]

        if customer:
            df = df[
                df["customer_id"].astype(str).str.contains(customer)
            ]

        if status != "All":
            df = df[
                df["order_status"] == status
            ]

        if payment != "All":
            df = df[
                df["payment_status"] == payment
            ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        selected_order = st.selectbox(
            "Select Order",
            df["order_id"]
        )

        detail = requests.get(
            f"{API_URL}/orders/{selected_order}"
        ).json()

        st.header(f"📦 Order #{selected_order}")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📄 Order",
            "🛒 Items",
            "💳 Payment",
            "🚚 Shipment",
            "🤖 AI Investigation"
        ])

        # ----------------------------------------------------
        # Order
        # ----------------------------------------------------

        with tab1:

            c1, c2 = st.columns(2)

            with c1:

                st.write(f"**Customer ID:** {detail['customer_id']}")
                st.write(f"**Status:** {detail['order_status']}")
                st.write(f"**Payment:** {detail['payment_status']}")

            with c2:

                st.write(f"**Total:** ₹{detail['total_amount']}")
                st.write(f"**Created:** {detail['created_at']}")

        # ----------------------------------------------------
        # Items
        # ----------------------------------------------------

        with tab2:

            items = requests.get(
                f"{API_URL}/orders/{selected_order}/items"
            ).json()

            st.dataframe(
                pd.DataFrame(items),
                use_container_width=True
            )

        # ----------------------------------------------------
        # Payment
        # ----------------------------------------------------

        with tab3:

            payment = requests.get(
                f"{API_URL}/orders/{selected_order}/payment"
            ).json()

            st.json(payment)

        # ----------------------------------------------------
        # Shipment
        # ----------------------------------------------------

        with tab4:

            shipment = requests.get(
                f"{API_URL}/orders/{selected_order}/shipment"
            ).json()

            st.json(shipment)

        # ----------------------------------------------------
        # AI
        # ----------------------------------------------------

        with tab5:

            if st.button("Investigate Order"):

                result = requests.get(
                    f"{API_URL}/orders/{selected_order}/investigate"
                )

                st.success(result.json()["analysis"])

    else:

        st.error("Unable to fetch orders.")
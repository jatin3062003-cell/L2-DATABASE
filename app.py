import streamlit as st

from ui.dashboard import show as dashboard_page
from ui.customer import show as customer_page
from ui.order import show as orders_page
from ui.payment import show as payments_page
from ui.transaction import show as transactions_page
#from ui.shipments import show as shipments_page
from ui.refund import show as refunds_page
from ui.chat import show as ai_page
#from ui.accounts import show as accounts_page
#from ui.wallets import show as wallets_page
#from ui.ai_assistant import show as ai_page

st.set_page_config(
    page_title="L2 Database Support Portal",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Sidebar ----------------

with st.sidebar:

    st.title("🛠️ L2 Portal")
    st.caption("Database Support Console")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🤖 AI Assistant",
            "👥 Customers",
            "📦 Orders",
            "💳 Payments",
            "💸 Transactions",
            # "🚚 Shipments",
            "💰 Refunds",
            # "🏦 Accounts",
            # "👛 Wallets",
             
        ],
        label_visibility="collapsed"
    )

    st.divider()

    

# ---------------- Main Area ----------------

if page == "🏠 Dashboard":
    dashboard_page()

elif page == "👥 Customers":
    customer_page()

elif page == "📦 Orders":
    orders_page()

elif page == "💳 Payments":
    payments_page()

elif page == "💸 Transactions":
    transactions_page()

# elif page == "🚚 Shipments":
#     shipments_page()

elif page == "💰 Refunds":
    refunds_page()

# elif page == "🏦 Accounts":
#     accounts_page()

# elif page == "👛 Wallets":
#     wallets_page()

elif page == "🤖 AI Assistant":
    ai_page()
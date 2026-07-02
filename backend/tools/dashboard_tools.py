from langchain_core.tools import tool

from services.dashboard_service import dashboard


@tool
def dashboard_summary():
    """
    Returns dashboard statistics including
    customers,
    orders,
    failed payments,
    pending refunds.
    """
    return dashboard()
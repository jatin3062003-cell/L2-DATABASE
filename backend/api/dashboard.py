from fastapi import APIRouter
from database import get_connection
from main import ask_agent

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard():
   conn = get_connection()
   cursor = conn.cursor()

   data = {}

   data["customers"] = cursor.execute(
        "SELECT COUNT(*) FROM customers"
    ).fetchone()[0]

   data["orders"] = cursor.execute(
        "SELECT COUNT(*) FROM orders"
    ).fetchone()[0]

   data["payments"] = cursor.execute(
        "SELECT COUNT(*) FROM payments"
    ).fetchone()[0]

   data["shipments"] = cursor.execute(
        "SELECT COUNT(*) FROM shipments"
    ).fetchone()[0]

   data["wallets"] = cursor.execute(
        "SELECT COUNT(*) FROM wallets"
    ).fetchone()[0]

   data["failed_payments"] = cursor.execute(
        """
        SELECT COUNT(*)
        FROM payments
        WHERE payment_status='FAILED'
        """
    ).fetchone()[0]

   data["pending_refunds"] = cursor.execute(
        """
        SELECT COUNT(*)
        FROM refunds
        WHERE refund_status='PENDING'
        """
    ).fetchone()[0]

   revenue = cursor.execute(
        """
        SELECT SUM(amount)
        FROM payments
        WHERE payment_status='SUCCESS'
        """
    ).fetchone()[0]

   data["revenue"] = revenue or 0

   conn.close()

   return data
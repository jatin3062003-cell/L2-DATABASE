from fastapi import FastAPI
from api.customer import router as customer_router
from api.chat import router as chat_router
from api.order import router as order_router
from api.payment import router as payment_router
from  api.dashboard import router as dashboard_router
from  api.refund import router as refund_router
from api.transaction import router as transaction_router

app = FastAPI(
    title="L2 Database AI Assistant",
    version="1.0"
)

app.include_router(chat_router)
app.include_router(customer_router)
app.include_router(order_router)
app.include_router(dashboard_router)
app.include_router(payment_router)
app.include_router(refund_router)
app.include_router(transaction_router)

@app.get("/")
def home():
    return {
        "message": "L2 Database AI Assistant is running"
    }
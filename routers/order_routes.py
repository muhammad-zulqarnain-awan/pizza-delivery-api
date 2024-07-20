from fastapi import APIRouter

order_router = APIRouter(
    prefix="/orders",
    tags=['Order']
)


@order_router.get("/")
def order_root():
    return {"message": "Order Router"}
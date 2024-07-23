from fastapi import APIRouter

order_route = APIRouter(
    prefix='/order',
    tags=['order']
)

@order_route.get("/")
def root():
    return {"message": "Order Routes"}
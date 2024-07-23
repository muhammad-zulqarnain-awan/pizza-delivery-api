from routers import auth_routes, order_routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_routes.auth_route)
app.include_router(order_routes.order_route)
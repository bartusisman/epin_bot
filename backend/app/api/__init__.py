from fastapi import APIRouter
from app.api.endpoints import orders, users, admin

api_router = APIRouter()
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])

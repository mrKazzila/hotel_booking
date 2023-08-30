from fastapi import FastAPI

from app.bookings.router import router as booking_router
from app.users.router import router as users_router

app = FastAPI()
app.include_router(router=users_router)
app.include_router(router=booking_router)

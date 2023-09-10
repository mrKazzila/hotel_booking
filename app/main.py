from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as booking_router
from app.hotels.router import router as hotels_router
from app.images.router import router as images_router
from app.pages.router import router as pages_router
from app.rooms.router import router as rooms_router
from app.settings.redis_setup import redis_setup
from app.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Service started')
    await redis_setup()
    yield
    print("Service exited")


app = FastAPI(lifespan=lifespan)

app.mount(
    path='/static',
    app=StaticFiles(directory='app/static'),  # TODO: move to settings
    name='static',
)

app.include_router(router=users_router)
app.include_router(router=booking_router)
app.include_router(router=hotels_router)
app.include_router(router=rooms_router)
app.include_router(router=pages_router)
app.include_router(router=images_router)

origins = ['http://localhost:3000']  # TODO: move to env

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=[
        'Content-Type', 'Set-Cookie',
        'Access-Control-Allow-Headers', 'Access-Control-Allow-Origin',
        'Authorization',
    ],
)

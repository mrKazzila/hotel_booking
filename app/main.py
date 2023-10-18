import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin

from app.admin_panel.auth import authentication_backend
from app.admin_panel.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UsersAdmin
from app.bookings.router import router as booking_router
from app.hotels.router import router as hotels_router
from app.images.router import router as images_router
from app.pages.router import router as pages_router
from app.rooms.router import router as rooms_router
from app.settings.config import settings
from app.settings.database import engine
from app.settings.redis_setup import redis_setup
from app.settings.sentry_setup import sentry_setup
from app.users.router import router as users_router

logger = logging.getLogger(__name__)

ADMIN_VIEWS = (UsersAdmin, BookingsAdmin, HotelsAdmin, RoomsAdmin)
ROUTERS = (users_router, booking_router, hotels_router, images_router, pages_router, rooms_router)


@asynccontextmanager
async def lifespan():
    logger.info('Service started')
    await redis_setup()

    yield

    logger.info('Service exited')


sentry_setup()
app = FastAPI(lifespan=lifespan)

admin = Admin(
    app=app,
    engine=engine,
    title='Booking Admin',
    authentication_backend=authentication_backend,
)

for admin_view in ADMIN_VIEWS:
    admin.add_view(admin_view)

for router_ in ROUTERS:
    app.include_router(router=router_)

app.mount(
    path='/static',
    app=StaticFiles(directory=settings().STATIC_PATH),
    name='static',
)
origins = [f'{settings().DOMAIN}:{settings().DOMAIN_PORT}']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization',
    ],
)

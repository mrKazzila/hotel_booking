from celery import Celery

from app.settings.config import settings

celery_app = Celery(
    'celery_service',
    broker=f'{settings().REDIS_HOST}:{settings().REDIS_PORT}',
)
# if test_tmp > 0:

celery_app.autodiscover_tasks(
    [
        'app.images',
        'app.bookings',
    ],
)

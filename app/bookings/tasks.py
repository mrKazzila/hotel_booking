import smtplib
import asyncio

from pydantic import EmailStr

from app.core.email_templates import create_booking_confirmation_template
from app.settings.celery_app import celery_app
from app.settings.config import settings
from app.bookings.services import BookingServices


async def get_booking_info(booking_id: int):
    print('get_booking_info')
    return await BookingServices.find_user_booking_by_id(booking_id=booking_id)


@celery_app.task(name='Booking confirmation')
def send_booking_confirmation_email(booking_id: int, email_to: EmailStr):
    # TODO: get information about booking from db
    # booking_info = asyncio.run(BookingServices.find_user_booking_by_id(booking_id=booking_id))

    booking_info = 'test'
    email_content = create_booking_confirmation_template(booking=booking_info, email_to=email_to)

    with smtplib.SMTP_SSL(settings().SMTP_HOST, settings().SMTP_PORT) as smtp_server:
        smtp_server.login(settings().SMTP_USER, settings().SMTP_PASS)
        smtp_server.send_message(email_content)

    return

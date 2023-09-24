from email.message import EmailMessage

from pydantic import EmailStr

from app.settings.config import settings


def create_booking_confirmation_template(booking, email_to: EmailStr):
    print(f'{booking=}')
    email = EmailMessage()

    email['Subject'] = 'Booking confirmation'
    email['From'] = settings().SMTP_USER
    email['To'] = email_to

    email.set_content(
        """
        <h1>Please confirm your booking!</h1>
        <br>

        You booked hotel
        """,
        subtype='html',
    )

    return email

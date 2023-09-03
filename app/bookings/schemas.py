from datetime import date, datetime, timezone

from pydantic import BaseModel, field_validator, model_validator


class SAddBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

    @field_validator('date_from')
    def __validate_date_from(cls, v: date) -> date:
        current_day_ = datetime.utcnow().date()
        current_day = datetime.combine(current_day_, datetime.min.time())

        current_date_timestamp = int(current_day.timestamp())
        date_from_timestamp = int(datetime.combine(v, datetime.min.time()).timestamp())

        if current_date_timestamp > date_from_timestamp:
            raise ValueError('date_from должен быть больше или равен текущей дате')
        return v

    @field_validator('date_to')
    def __validate_date_to(cls, v: date) -> date:
        date_to = int(datetime(v.year, v.month, v.day).timestamp())
        current_date = int(datetime.now(timezone.utc).timestamp())

        if date_to <= current_date:
            raise ValueError('date_to должен быть больше текущей даты')
        return v

    @model_validator(mode='after')
    def __validate_dates(self):
        date_from = self.date_from
        date_to = self.date_to

        if date_to <= date_from:
            raise ValueError('date_to должно быть больше, чем date_from')

        return self


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


class SUserBookings(BaseModel):
    user_id: int
    room_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    image_id: int
    name: str
    description: str
    services: list[str]


class SDeletedUserBooking(BaseModel):
    id: int
    user_id: int
    room_id: int
    date_from: date
    date_to: date

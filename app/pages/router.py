from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from app.hotels.router import get_hotels

router = APIRouter(
    prefix='/pages',
    tags=['Frontend'],
)

templates = Jinja2Templates(directory='app/templates')  # todo: move to settings


@router.get('/hotels')
async def get_hotels_page(request: Request, hotels=Depends(get_hotels)):
    return templates.TemplateResponse(
        name='hotels.html',
        context={
            'request': request,
            'hotels': hotels,
        },
    )



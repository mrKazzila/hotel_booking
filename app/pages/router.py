from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_hotels
from app.settings.config import settings

router = APIRouter(
    prefix='/pages',
    tags=['Frontend'],
)

templates = Jinja2Templates(directory=settings().TEMPLATES_PATH)


@router.get('/hotels')
async def get_hotels_page(request: Request, hotels=Depends(get_hotels)):
    return templates.TemplateResponse(
        name='hotels.html',
        context={
            'request': request,
            'hotels': hotels,
        },
    )

import shutil

from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse

from app.images.tasks import image_process
from app.settings.config import settings

router = APIRouter(
    prefix='/images',
    tags=['Uploading files'],
)


@router.post('/hotels')
async def add_hotel_images(name: int, file: UploadFile):
    static_path = settings().STATIC_PATH
    image_path = f'{static_path}/images/{name}.webp'

    with open(image_path, 'wb+') as image_file_object:
        shutil.copyfileobj(file.file, image_file_object)

        image_process.delay(image_path)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={'details': f'Success upload file {image_file_object.name}'}
        )

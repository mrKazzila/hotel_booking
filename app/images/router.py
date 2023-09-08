from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
import shutil


router = APIRouter(
    prefix='/images',
    tags=['Uploading files'],
)


@router.post('/hotels')
async def add_hotel_images(name: int, file: UploadFile):
    with open(f'app/static/images/{name}.webp', 'wb+') as image_file_object:
        shutil.copyfileobj(file.file, image_file_object)
        return JSONResponse(
            status_code=201,
            content={'details': f'Success upload file {image_file_object.name}'}
        )

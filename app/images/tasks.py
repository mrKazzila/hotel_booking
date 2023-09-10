from enum import Enum
from pathlib import Path

from PIL import Image

from app.settings.celery_app import celery_app
from app.settings.config import settings


class ImageSize(Enum):
    MEDIUM: tuple = (1000, 500)
    SMALL: tuple = (200, 100)


@celery_app.task(name='Resize images')
def image_process(path: str):
    image_path = Path(path)
    image_object = Image.open(image_path)

    resize_image(image_obj=image_object, image_name=image_path.name)


def resize_image(image_obj: Image, image_name: Path.name):
    for size_ in ImageSize:
        resize_image_obj = image_obj.resize(size_.value)

        size_type_lower = size_.name.lower()
        static_path = settings().STATIC_PATH

        resize_image_obj.save(f'{static_path}/images/{size_type_lower}_{image_name}')

import os
import uuid
from django.conf import settings

from celery.task import task

import osaic

from core.models import Mosaic
from core.utils import DownloadManager


@task(ignore_result=True)
def make_mosaic(pics_urls, user):
    output_directory = os.path.join(settings.USERPICS_DIR, str(user.id))
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    downloader = DownloadManager(download_list=pics_urls, output_directory=output_directory)
    downloader.begin_downloads()
    pics_files = [os.path.join(output_directory, x) for x in os.listdir(output_directory)]
    output_filename = os.path.join(settings.MOSAICS_DIR, uuid.uuid1().hex + '.png')
    osaic.mosaicify(
        target=user.image.path,
        sources=pics_files,
        tiles=40,
        zoom=8,
        output=output_filename,
    )
    mosaic = Mosaic(user=user)
    mosaic.image.name = output_filename[len(settings.MEDIA_ROOT) + 1:]
    mosaic.save()
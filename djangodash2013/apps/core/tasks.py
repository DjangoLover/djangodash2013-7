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
        #downloader = DownloadManager(download_list=pics_urls, output_directory=output_directory)
    #downloader.begin_downloads()
    pics_files = [os.path.join(output_directory, x) for x in os.listdir(output_directory)]
    output_filename = 'lol.png'
    osaic.mosaicify(
        target='/Users/franz/Downloads/193935_1885255421064_1288446_o.jpg',
        sources=pics_files,
        tiles=40,
        zoom=2,
        output=output_filename,
    )
    Mosaic.objects.create(user=user, image_path=output_filename)
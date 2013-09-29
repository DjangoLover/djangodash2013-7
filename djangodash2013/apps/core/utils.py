import os
import Queue
import threading
import requests

from django_facebook.api import FacebookUserConverter, get_facebook_graph


def get_facebook_friends(request):
    open_graph = get_facebook_graph(request)
    converter = FacebookUserConverter(open_graph)
    friends = converter.open_facebook.fql(
        u'SELECT uid, name, birthday, sex FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())')
    return friends


class _Downloader(threading.Thread):
    def __init__(self, queue, output_directory):
        threading.Thread.__init__(self, name=os.urandom(16).encode('hex'))
        self.queue = queue
        self.output_directory = output_directory

    def run(self):
        while True:
            url = self.queue.get()
            self.download_file(url)
            self.queue.task_done()

    def download_file(self, url):
        r = requests.get(url)
        if (r.status_code == requests.codes.ok):
            fname = self.output_directory + "/" + os.path.basename(url)
            with open(fname, "wb") as f:
                f.write(r.content)
        else:
            pass


class DownloadManager():
    def __init__(self, download_list, output_directory, thread_count=5):
        self.thread_count = thread_count
        self.download_list = download_list
        self.output_directory = output_directory

    def begin_downloads(self):
        queue = Queue.Queue()
        threads = list()

        for i in range(self.thread_count):
            thread = _Downloader(queue, self.output_directory)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)

        for link in self.download_list:
            queue.put(link)
        for thread in threads:
            thread.join()
        return


def get_friends_pics(request):
    from core.tasks import make_mosaic

    open_graph = get_facebook_graph(request)
    converter = FacebookUserConverter(open_graph)
    pics_raw = converter.open_facebook.fql(
        u'SELECT pic FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())')
    pics = [x['pic'] for x in pics_raw]
    make_mosaic.apply_async(kwargs=dict(user=request.user, pics_urls=pics))
    return
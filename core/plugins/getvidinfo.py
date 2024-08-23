from core import *
from core.plugins.cfg import *
from core.plugins.log import *
from core.plugins.sess import *

class getvidinfo:
    def get():
        ses, headers = sess.get()

        r = ses.get(
            f'https://tiktok.livecounts.io/video/stats/{cfg().get().rsplit("/", 1)[-1]}', 
            headers=headers
        )

        if r.json()['success'] == True:
            return r.json()['viewCount'], r.json()['likeCount'], r.json()['commentCount'], r.json()['shareCount']
        else:
            log.error('GET VID INFO', r.text)
            getvidinfo.get()
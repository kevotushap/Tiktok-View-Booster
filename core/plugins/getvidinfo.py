from core import *
from core.plugins.cfg import *
from core.plugins.log import *
from core.plugins.sess import *

class getvidinfo:
    def get(retries=0):
        ses, headers = sess.get()

        headers['Authority'] = 'tiktok.livecounts.io'
        headers['Origin'] = 'https://livecounts.io'

        r = ses.get(
            f'https://tiktok.livecounts.io/video/stats/{cfg().get().rsplit('/', 1)[-1]}', 
            headers=headers
        )

        if r.json()['success'] == True:
            return r.json()['viewCount'], r.json()['likeCount'], r.json()['commentCount'], r.json()['shareCount']
        else:
            retries += 1
            log.error('GET VID INFO', r.text)
            if retries > 3:
                return '???' * 4

            getvidinfo.get(retries)
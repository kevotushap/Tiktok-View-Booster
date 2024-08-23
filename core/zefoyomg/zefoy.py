from core import *
from core.plugins.utils import utils
from core.plugins.log import log
from core.plugins.cfg import *
from core.plugins.solver import *

class zefoy:
    def __init__(self, video_url: str):
        self.session = tls_client.sessions.Session(
            client_identifier='chrome_120',
            random_tls_extension_order=True
        )
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-GB,en;q=0.6',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://zefoy.com'
        }

        self.phpsessid = random.choice(['jtc6tdfgs4tike6rs5in97gb77', 'lsaigisdllrkrdmqafn11qtk56', 'asr29bksl92cuim29u9ga0o1f4', 'gfoesubki0or0vqn1qpscs0ds6'])
        self.randphpid = uuid.uuid4().hex[:26]
        self.id = ''
        self.vid_key = ''

        self.video = video_url
        match = re.search(r'/(\d+)$', self.video)
        self.video_id = match.group(1)

        self.captcha_name = uuid.uuid4().hex[:6]
        self.captcha = {}

    def get_captcha(self):
        while True:
            r = self.session.get(
                'https://zefoy.com/',
                headers=self.headers,
                cookies={
                    'PHPSESSID': self.randphpid
                }
            )

            if r.status_code == 200:
                log.info('CAPTCHA FETCH', 'Sent a request to the site')
                match = re.search(r'<input\s+[^>]*name="([^"]+)"', r.text)
                if match:
                    self.id = match.group(1)

                match = re.search(r'<img\s+[^>]*src="([^"]+)"', r.text)
                if match:
                    link = match.group(1)
                    log.info('CAPTCHA FETCH', f'Captcha link found {link[:25]}...')

                    new_timestamp = utils.gen_timestamp()
                    link = re.sub(r'&amp;t=[0-9.]+\+[0-9]+', new_timestamp, link)
                    log.info('CAPTCHA FETCH', f'Replaced the timestamp {link[:25]}...')

                    r = requests.get(
                        f'https://zefoy.com/{link}',
                        headers=self.headers,
                        cookies={
                            'PHPSESSID': self.randphpid
                        }
                    )

                    open(f'captchas\\{self.captcha_name}.png', 'wb').write(r.content)
                    log.info('CAPTCHA FETCH', f'Got captcha and saved it to captchas\\{self.captcha_name}.png')
                    break

                else:
                    log.error('CAPTCHA FETCH', 'Captcha link not found')
                    time.sleep(2.5)
                    continue

            else:
                log.error('CAPTCHA FETCH', f'{r.status_code} {r.text}')
                time.sleep(2.5)
                continue
    
    def send_captcha(self):
        succes, answer = solver.solve(f'captchas\\{self.captcha_name}.png')

        try:
            os.remove(f'captchas\\{self.captcha_name}.png')
            log.info('CAPTCHA SEND', 'Removed captcha image')
        except Exception as e :
            log.error('CAPTCHA SEND', f'Failed to delete the captcha image > {e}')

        if succes == False:
            return False

        try:
            self.phpsessionID = self.session.cookies.get('PHPSESSID')
            self.session.cookies.set('PHPSESSID', self.phpsessionID, domain='zefoy.com')
        except:
            pass

        self.captcha[self.id] = answer 
        r = self.session.post(
            'https://zefoy.com/',
            headers=self.headers,
            data=self.captcha
        )

        if r.status_code == 200:
            log.info('CAPTCHA SEND', 'Captcha sent')
            if 'Captcha code is incorrect.' in r.text:
                log.info('CAPTCHA SEND', 'INVALID CAPTCHA PASSED')
                return False
            
        if 'Enter Video URL' in r.text:
            self.vid_key = r.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
            return True
        
        elif r.status_code == 302:
            log.info('CAPTCHA SEND', 'INVALID CAPTCHA PASSED')
            return False

        else:
            log.error('CAPTCHA SEND', f'{r.status_code} {r.text}')

        return True
    
    def parse_vid(self) -> str:
        try:
            while True:
                headers = self.headers
                headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ'
                headers['Origin'] = 'https://zefoy.com'

                data = f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.vid_key}"\r\n\r\n{cfg().get()}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n'

                r = self.session.post(
                    f'https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V', 
                    headers=headers, 
                    data=data
                )
                
                vid_info = base64.b64decode(unquote(r.text.encode()[::-1])).decode()

                if 'Session expired. Please re-login' in vid_info:
                    self.send_captcha()
                    return
                
                elif """onsubmit="showHideElements""" in vid_info:
                    if '" name="' in vid_info:
                        vid_info = [vid_info.split('" name="')[1].split('"')[0]]
                        return vid_info[0]
                    else:
                        log.error('PARSE VID', 'Expected pattern not found in vid_info')
                        return None
                
                elif 'Checking Timer...' in vid_info:
                    timer = int(re.findall(r'ltm=(\d*);', vid_info)[0])
                    log.info('PARSE VID', f'On timer for {timer} secs')
                    time.sleep(timer)
                    log.info('PARSE VID', f'Timer finished!')

                    r = self.session.post(
                        f'https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V', 
                        headers=headers, 
                        data=data
                    )

                    vid_info = base64.b64decode(unquote(r.text.encode()[::-1])).decode()
                    
                    if '" name="' in vid_info:
                        vid_info = [vid_info.split('" name="')[1].split('"')[0]]
                        return vid_info[0]
                    else:
                        log.error('PARSE VID', 'Expected pattern not found in vid_info')
                        return None
                
                else:
                    return vid_info
                
        except Exception as e:
            log.error('PARSE VID', e)

        
    def send_views(self):
        try:
            video_info = self.parse_vid()
            if video_info is None:
                self.parse_vid()

            token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            headers = self.headers
            headers['Content-Type'] = f'multipart/form-data; boundary=----WebKitFormBoundary{token}'
            
            data = f'------WebKitFormBoundary{token}\r\nContent-Disposition: form-data; name="{video_info}"\r\n\r\n{cfg().get().rsplit('/', 1)[-1]}\r\n------WebKitFormBoundary{token}--\r\n'

            r = self.session.post(
                'https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V',
                headers=headers,
                data=data
            )

            decoded = base64.b64decode(unquote(r.text.encode()[::-1])).decode()

            if 'Too many requests. Please slow down.' in decoded:
                log.info('SEND VIEWS', 'Got ratelimited... Retrying in 10 seconds')
                time.sleep(10)
                self.send_views()
            else:
                log.info('SEND VIEWS', 'Sending views...')
                try:
                    if 'Successfully 1000 views sent.' in decoded:
                        log.info('SEND VIEWS', '1000 Views sent!')
                    else:
                        log.info('SEND VIEWS', decoded.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])
                except:
                    timer = int(re.findall(r'ltm=(\d*);', decoded)[0])
                    time.sleep(timer)
                    data = f'------WebKitFormBoundary{token}\r\nContent-Disposition: form-data; name="{video_info}"\r\n\r\n{cfg().get().rsplit('/', 1)[-1]}\r\n------WebKitFormBoundary{token}--\r\n'
                    r2 = self.session.post(
                        f'https://zefoy.com/c2VuZC9mb2xeb3dlcnNfdGlrdG9V', 
                        headers=headers, 
                        data=data
                    )

                    decoded2 = base64.b64decode(unquote(r2.text.encode()[::-1])).decode()
                    if 'Successfully 1000 views sent.' in decoded2:
                        log.info('SEND VIEWS', '1000 Views sent!')
                    else:
                        log.info('SEND VIEWS', decoded2.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])
                    
                    self.send_captcha()

        except Exception as e:
            log.error('SEND VIEWS', e)

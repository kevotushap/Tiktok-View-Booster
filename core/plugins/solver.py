from core import *
from core.plugins.log import log

class solver:
    def solve(file: str) -> Tuple[bool, str]:
        image_file_descriptor = open(file, 'rb')
        files = {
            'image': image_file_descriptor
        }

        r = requests.post(
            'https://api.api-ninjas.com/v1/imagetotext', 
            files=files
        )

        #print(r.text)
        #print(r.status_code)

        if r.status_code == 200:
            try:
                answer = r.json()[0]['text'].strip()
            except:
                return False, ''
            
            log.info('CAPTCHA SOLVER', f'Solved captcha {answer}')
            return True, answer

        else:
            log.error('CAPTCHA SOLVER', f'{r.status_code} {r.text}')
            return False, ''
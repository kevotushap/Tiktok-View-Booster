from core import *

class sess:
    def get(tls_client=None):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        }

        sess = tls_client.Session(
            client_identifier='chrome_120',
            random_tls_extension_order=True
        )

        return sess, headers
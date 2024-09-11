from core import *

class utils:
    def gen_timestamp(self):
        fraction = f'{random.uniform(0, 1):.8f}'
        epoch_time = int(time.time())
        return f'&amp;t={fraction}+{epoch_time}'
    
    def decode(encoded):
        def rev_str(s):
            return s[::-1]

        reversed = rev_str(encoded)
        url_decoded = urllib.parse.unquote(reversed)
        missing_padding = len(url_decoded) % 4
        if missing_padding:
            url_decoded += '=' * (4 - missing_padding)

        decoded_bytes = base64.b64decode(url_decoded)
        decoded = decoded_bytes.decode('utf-8', errors='ignore')
        return decoded
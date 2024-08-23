import os
try:
    import requests
    import tls_client
    import string
    from typing import Tuple
    import pystyle
    import time
    import random
    import re
    import uuid
    import json
    import datetime
    import base64
    import urllib.parse
    from colorama import Fore, Back, init, Style as S; init(autoreset=True)
    from urllib.parse import urlparse, unquote
except ModuleNotFoundError:
    libs = [
        'requests',
        'tls-client',
        'uuid',
        'datetime',
        'colorama',
        'pystyle'
    ]

    for lib in libs:
        os.system(f'pip install {lib}')

    input('Installed all libs! Please re run!!!')

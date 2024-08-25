import os; os.system('title Tiktok View Booster')
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
    import threading
    import json
    import datetime
    import base64
    import urllib.parse
    from colorama import Fore, Back, init, Style as S; init(autoreset=True)
    from urllib.parse import urlparse, unquote

except ModuleNotFoundError as e:
    libs = [
        'requests',
        'tls-client',
        'uuid',
        'datetime',
        'colorama',
        'pystyle',
        'typing-extensions',
        'typing_extensions'
    ]

    for lib in libs:
        os.system(f'pip install {lib}')

    input('Installed all libs! Please re run!')
    
start_time = time.time()

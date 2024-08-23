import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from core import *
from core.zefoyomg.zefoy import zefoy
from core.plugins.log import *
from core.plugins.ui import *
from core.plugins.cmd import *
from core.plugins.cfg import *

def main():
    cmd.cls()
    UI.banner()
    print('\n')
    UI.stats()
    print('\n')

    threading.Thread(target=cmd.thread_title).start()

    log.info('PROXY SCRAPER', 'Scraping proxies...')
    proxies = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&simplified=true').text
    with open('proxies.txt', 'w') as f:
        f.write(proxies.replace('\n', ''))
    log.info('PROXY SCRAPER', 'Scraping proxies...') 

    while True:
        zef = zefoy(cfg().get())
        solve_success = False
        while not solve_success:
            zef.get_captcha()
            solve_success = zef.send_captcha()

        zef.parse_vid()
        zef.send_views()

if __name__ == '__main__':
    main()
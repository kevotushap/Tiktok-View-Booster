import sys, os
import requests  # Ensure you import requests if not already imported

sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

from core import *
from core.zefoyomg.zefoy import zefoy
from core.plugins.log import log  # Correctly import the log instance
from core.plugins.ui import UI
from core.plugins.cmd import cmd
from core.plugins.cfg import cfg

def main():
    try:
        # Create an instance of cmd and call cls()
        command_instance = cmd()
        command_instance.cls()  # Call the method on the instance

        # Create an instance of UI and call banner()
        ui_instance = UI()
        ui_instance.banner()  # Call banner() on the instance

        print('\n')

        log.info('PROXY SCRAPER', 'Scraping proxies...')

        # Scrape proxies and save them to proxies.txt
        proxies = requests.get(
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&simplified=true').text
        with open('proxies.txt', 'w') as f:
            f.write(proxies.replace('\n', ''))

        log.info('PROXY SCRAPER', 'Proxies scraped successfully!')

        # Loop for Zefoy captcha and view sending
        while True:
            zef = zefoy(cfg().get())  # Create an instance of zefoy class
            solve_success = False

            # Solve captcha until successful
            while not solve_success:
                zef.get_captcha()
                solve_success = zef.send_captcha()

            # Parse video and send views
            zef.parse_vid()
            zef.send_views()

    except Exception as e:
        log.error('GENERAL ERROR', f'An error occurred: {e}')

if __name__ == '__main__':
    main()

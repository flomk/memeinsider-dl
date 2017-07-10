#!/usr/bin/env python3

import argparse
import re
import random
import requests

from utils import *
from termcolor import cprint
from requests.sessions import Session

s = requests.Session()
headers = {
    'Host': 'memeinsider.co',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:55.0) Gecko/20100101 Firefox/55.0'
}


def meme(url):
    log_info('[+] Downloading webpage...')
    webpage = s.get(url, headers=headers).text
    if webpage:
        log_success('[*] Successfully downloaded webpage!')
    else:
        log_error('[-] Error downloading webpage')
    title = url.split('/')[-1]
    issue_url = re.findall(r'var\surl\s=\s\"(.+)\";', webpage)[0]
    log_info('[+] Downloading pdf...')
    r = s.get(issue_url)
    if r:
        pass
    else:
        log_error('[-] Error downloading webpage')

    with open(f'{title}.pdf', 'wb') as pdf:
        pdf.write(r.content)
        log_success('[*] Done')


def main():
    parser = argparse.ArgumentParser(description='Usage: memeinsider-dl [URL]')
    args1 = parser.add_argument('url', help="download issue",)
    args = parser.parse_args()
    bleh = args.url
    meme(bleh)


if __name__ == '__main__':
    print("""                                  _            _     __                    ____
   ____ ___  ___  ____ ___  ___  (_)___  _____(_)___/ /__  _____      ____/ / /
  / __ `__ \/ _ \/ __ `__ \/ _ \/ / __ \/ ___/ / __  / _ \/ ___/_____/ __  / /
 / / / / / /  __/ / / / / /  __/ / / / (__  ) / /_/ /  __/ /  /_____/ /_/ / /
/_/ /_/ /_/\___/_/ /_/ /_/\___/_/_/ /_/____/_/\__,_/\___/_/         \__,_/_/
    """)
    main()

#!/usr/bin/env python

"""
Web Application Scandy is a web vulnerability scanner
Author: Andrews B. Okyere
Features: Header checks, sqli, info gathering
"""

from WascandyCore import *


class WebAppScandy(WascandyCore):

    def __init__(self):
        super().__init__()

    def security_headers(self):
        page = requests.get(self.args.url)

        return page.headers

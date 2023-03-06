#!/usr/bin/env python

import argparse
import sys

import requests


class WascandyCore:

    def __init__(self):
        self.url = None
        self.args = None
        self.ArgumentProcessor()
        self.url_validator()

    def ArgumentProcessor(self):
        parser = argparse.ArgumentParser(
            description=f"Web application vulnerability scanner",
            epilog=f"Example \r\npython {sys.argv[0]} -u example.com"
        )

        parser.add_argument('-u', '--url', help="url of the website to scan")
        parser.add_argument('--header', nargs='?', default=False,
                            help='Scan headers for security issues')

        self.args = parser.parse_args()
        self.url = self.args.url

        # header arg
        if self.args.header is None:
            self.args.header = True
            print("headers")

        return

    def url_validator(self):
        if "http" not in self.args.url:
            self.args.url = f"http://{self.args.url}"
        return

    def session_instance(self):
        session = requests.session()
        session.max_redirects = 2
        return session

    def getrequest(self, url, headers, timeout=3):
        """
        Used for GET request method from target page.
        :return: results
        """
        pass

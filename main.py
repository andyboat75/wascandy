#!/usr/bin/env python

from wascandy import WebAppScandy

def main():
    w = WebAppScandy()
    w.security_headers()


if __name__ == '__main__':
    main()

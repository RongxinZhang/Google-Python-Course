#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import errno
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    # NOTE: Hostname not longer exists
    hostName = 'http://'+ filename

    inFile = open(filename, 'r')
    urlList = []
    for line in inFile:
        match = re.search(r'"GET ([\S]+.jpg)', line)
        if match and match.group(1) not in urlList:
            urlList.append(match.group(1))

    for i, url in enumerate(urlList):
        urlList[i] = hostName + url

    # # NOTE: TEMP IMAGE
    urlList = ['http://a.abcnews.com/images/Business/GTY_stock_cash_pile_money_dollar_bills-thg-130726_33x16_1600.jpg']

    return sorted(urlList)


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  for i, url in enumerate(img_urls):
    match = re.search('(\.[\w]+$)', url)
    fileExt = '.jpg'

    if match and match.group(1): fileExt = match.group(1)

    directory = './' + dest_dir + '/img_' + str(i) + fileExt

    urllib.request.urlretrieve(url, directory)

def createHTML(htmlFile, images):
    imgs = ""
    for i in images:
        imgs = imgs + '<img src="{}">'.format(i)

    template = '<verbatim>  <html> <body> ' + imgs + ' </body>  </html>'

    with open(htmlFile,'w') as f:
        f.write(template + '\n')

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        try:
          os.makedirs(todir)
        except OSError as e:
          if e.errno != errno.EEXIST:
              raise

        download_images(img_urls, todir)
        
        fileName ='imageDisplay.html'
        createHTML(fileName, img_urls)
        print("HTML file created: {}".format(fileName))

if __name__ == '__main__':
  main()

'''
download flower dataset from : http://www.robots.ox.ac.uk/~vgg/data/flowers/102/
download caption dataset from : https://drive.google.com/uc?export=download&confirm=l7Ld&id=0B0ywwgffWnLLcms2WWJQRFNSWXM
'''
from __future__ import print_function
from six.moves import urllib
import requests
# import urllib2
import os
import sys


def download(url, dirpath):
	filepath = dirpath
	u = urllib.request.urlopen(url)
	f = open(filepath, 'wb')
	filesize = int(u.headers["Content-Length"])
	print("Downloading: %s Bytes: %s" % ("bird", filesize))

	downloaded = 0
	block_sz = 8192
	status_width = 70
	while True:
		buf = u.read(block_sz)
		if not buf:
			print('')
			break
		else:
			print('', end='\r')
		downloaded += len(buf)
		f.write(buf)
		status = (("[%-" + str(status_width + 1) + "s] %3.2f%%") %
			('=' * int(float(downloaded) / filesize * status_width) + '>', downloaded * 100. / filesize))
		print(status, end='')
		sys.stdout.flush()
	f.close()
	return filepath

if __name__ == '__main__':
	url = "http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz"
	cur_dir = os.getcwd()
	image_dir = os.path.join(cur_dir,"102flowers.tgz")
	download(url,image_dir)
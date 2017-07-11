#!/usr/bin/python

from __future__ import print_function
import pycurl, json, requests, pprint
import genpwd;
from io import BytesIO
from StringIO import StringIO



def recordPwd():
	global pwd
	pwd=genpwd.generate_pass()
	#print 'Password Generated!'
	#print 'Generated is :',pwd


def formCurl():
	recordPwd()

	#print 'Again:',pwd
	url = 'https://pwpush.com/p.json'
	payload = [
  ('password[payload]', pwd),
  ('password[expire_after_days]', '7'),
  ('password[expire_after_views]', '5'),
]
	response = requests.post(url, params=payload)
	data = json.loads(response.text)
	#print("Data Collected is :",data)
	token = data["url_token"]
	#print('Get Token for URL :',token)
	combineStr='https://pwpush.com/p/'
	combineStr += token
	print('Final URL is :',combineStr)
	#print('Final URL is : https://pwpush.com/p/',token, end='')
		

#curl -X POST --data "password[payload]=rab52e4ZMHLl1mYMGtX(m&password[expire_after_days]=7&password[expire_after_views]=5" https://pwpush.com/p.json
formCurl()

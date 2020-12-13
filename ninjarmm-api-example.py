#!/usr/bin/env python

""" ninjarmm_api_example.py: Example interaction with the NinjaRMM API. """

import requests
import datetime
import hashlib
import hmac
import base64

# api-endpoint
api_url = "http://api.ninjarmm.com"

# HMAC-SHA1 config
http_verb = "GET"
content_md5 = ""
content_type = ""
date = datetime.datetime.now(datetime.timezone.utc).strftime(
    "%a, %d %b %Y %H:%M:%S GMT")
canonicalized_resource = "/v1/customers"

secret_access_key = "the-access-key-goes-here"
access_key_ID = "ID-FOR-ACCESS-KEY-GOES-HERE"

string_to_sign = http_verb + "\n" + content_md5 + "\n" + content_type + "\n" \
    + date + "\n" + canonicalized_resource;

# From NinjaRMM Docs: Signature = Base64( HMAC-SHA1( YourSecretAccessKeyID,
#       Base64( UTF-8- Encoding-Of( StringToSign ) ) ) );
key = bytes(secret_access_key, 'UTF-8')
message = base64.urlsafe_b64encode(bytes(string_to_sign, 'UTF-8'))
digester = hmac.new(key, message, hashlib.sha1)
hex_result = digester.hexdigest()

signature = str(base64.urlsafe_b64encode(bytes.fromhex(hex_result)), 'UTF-8')
auth_param = "NJ " + access_key_ID + ":" + signature

# params
URL = api_url + canonicalized_resource
HEADERS = {'Host':'api.ninjarmm.com', 'Date':date, 'Authorization':auth_param}
PARAMS = {'StringToSign':string_to_sign}

# sending get request and saving the response as response object 
r = requests.get(url = URL, headers = HEADERS, params = PARAMS)

# extracting data in json format 
data = r.json() 

print(data)

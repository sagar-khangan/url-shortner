import tldextract
from db import *
import json

BASE_URL  = "http://"

def get_tld(url):
    ext = tldextract.extract(url)
    return (ext.registered_domain)

def get_short_url(url,base):
    try:
        tld = get_tld(url)
        shortcode = b'%04X' % (sum(str.encode(tld)) & 0xFFFF)
        short_code_str = shortcode.decode('cp1252')
        shorturl = BASE_URL+base+"/"+short_code_str
        save(url,shorturl,tld)
    except Exception as e:
        print(e)
        shorturl = None
    return shorturl

def get_raw_url(code,host):
    try:
        url = BASE_URL+host+"/"+code
        raw_url = get_url_by_shortcode(url)
        if 'http' not in raw_url:
            return  BASE_URL+raw_url
        return raw_url
    except Exception as e:
        print(e)
        
def get_all_url():
    return  get_url_all()

def del_short_url(url):
    return (delete_url(url))


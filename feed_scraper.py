import redis
from time import time
from celery import Celery
import requests
import urllib2, cookielib
import json
import feedparser

import os, sys, re, json

app = Celery("hello" )
app.config_from_object("celeryconfig")
# celery -A feed_scraper worker -B --loglevel=INFO

@app.task
def feeds():
    FILER_TITLE_RE      = re.compile(r'(.*) - (.*) \((.*)\) \((.*)\)')
    
   

    feed_url='http://feeds.bbci.co.uk/news/rss.xml'

    full_data   = feedparser.parse(feed_url)
    feed_list=[]
    for entry in full_data["entries"]:
        print entry
        try:
            link            = str(entry["link"])
            title_entries   = FILER_TITLE_RE.findall(str(entry["title"]))
            summary         = str(entry["summary"])
        

            new_hash    = {
                    
                        "Title" : str(entry["title"]),
                        "Summary"   : str(summary),
                        "URL"       : str(link)
                   
            }
            print type(new_hash)
            print new_hash
            feed_list.append(new_hash)
            #green_print("Entry(" + str(idx) + ") => Data(" + json.dumps(new_hash) + ")\n")
        except Exception,e:
            #red_print("ERROR: Failed to parse Entry(" + str(idx) + ") Data(" + str(entry) + ")")
            print ("error converting")
    
    
    print feed_list
    print type(feed_list[0])
    #insert into redis with data_list as key
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #replace the key value in redis at every function call
    r.delete('rss_list')
    for feed in feed_list:
        r.rpush('rss_list',json.dumps(feed))      

    #print r.lrange('data_list',0,-1)
    #r.hmset('data',content)
    return feed_list

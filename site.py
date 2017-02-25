import json
import redis
import cherrypy
from os import path, curdir

class StackMirror(object):
    @cherrypy.expose
    def index(self):
        return file("index.html")

    @cherrypy.expose
    def update(self, timestamp=None):
        try:
            timestamp = int(timestamp)
        except TypeError:
            timestamp = 0
        
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        

        #return data to frontend
        articles=r.lrange('rss_list',0,-1)
        print articles
        return json.dumps([json.loads(art) for art in articles])

cherrypy.quickstart(StackMirror(), "/", { "/static": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "static")}})

# Igninite-Solution


<<<<<<< HEAD
# Introduction 
Web app showing realtime RSS feed from BBC news website.
This app is based on a Cherry Backend with Redis as storage.
Celery has been used for scheduling calls to scrap latest data from BBC news website.
Read about CherryPy : http://cherrypy.org/ and read about Redis: https://redis.io/ and about Celery : http://www.celeryproject.org/

#Requirements
Please make sure that Rabbitmq(Default message broker for celery) and its dependencies have been installed.
Refer to: https://www.rabbitmq.com/install-rpm.html

Also install redis server using this link: https://redis.io/topics/quickstart

Python modules required have been mantioned in 'requirements.txt'

Please install it using: pip install -r requirements.txt 


#Deployment and testing 
For local deployment:
1. Start Redis server: redis-server
2. Start celery worker: celery -A feed_scraper worker -B --loglevel=INFO
3. Start the Cherrypy server: python site.py 





=======
# Igninite-Solution
>>>>>>> e933777df9a1184df3ee05deb0ff394a8253894e

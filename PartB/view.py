from flask import Flask, request, render_template, session, flash, redirect,url_for, jsonify
import os, sys, re, json,feedparser
app = Flask(__name__)

#to 
@app.route('/')
def get_rss_link():
    return render_template('home.html')


@app.route('/headlines',methods=['POST','GET'])
def feeds():
    if request.method=='POST':
        feed_url=request.form['search']

    FILER_TITLE_RE      = re.compile(r'(.*) - (.*) \((.*)\) \((.*)\)')
    full_data   = feedparser.parse(feed_url)
    print feed_url
    feed_list=[]
    for entry in full_data["entries"]:
        print entry
        try:
            link            = str(entry["link"])
            title_entries   = FILER_TITLE_RE.findall(str(entry["title"]))
            summary         = str(entry["summary"])
        

            new_hash    = {
                    
                        "Title" : str(entry["title"]),
                        # "Title"     :srt(title_entries),
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
    #returning data to frontend
    if(len(feed_list)==0):
        return render_template('error.html')

    feed_json_object={}
    #'data' is the key of our new json object
    feed_json_object['data']=[]
    for articles in feed_list:
        feed_json_object['data'].append(articles)
    print type(feed_json_object)
    return render_template("headline.html",feed_json_object=feed_json_object)
    
if __name__ == '__main__':
   

    app.run(
        host="127.0.0.1",
        port=int("5000"),
        debug=True
    )


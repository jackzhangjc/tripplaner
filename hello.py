from restaurants import query_api
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/yelp")
def restaraunts():
    bizs = query_api("sushi", "Toronto, ON") 
    out = "<ul>"
    for b in bizs:
	out += "<li><img src=\'%s\'></li>" % b['image_url']
    out += "</ul>"
    return out

if __name__ == "__main__":
    app.run()

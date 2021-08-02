# - *- coding: utf- 8 - *-

from datetime import datetime

from flask import Flask 
from req import get_weather


city_id = "id"
apikey = "text"

app = Flask(__name__) 


@app.route("/") 
def index(): 
    url = "text" % (city_id, apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%D.%m.%Y')

    result = "<p><b>Temperature:</b> %s</p>" % weather['main']['temp']
    result += "<p><b>City:</b> %s</p>" % weather['name']
    result += "<p><b>Date:</b> %s</p>" % cur_date
    return result


if __name__ == "__main__": 
    app.run(port=text, debug=True)

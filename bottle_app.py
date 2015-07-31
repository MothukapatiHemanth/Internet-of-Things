from bottle import default_app, route, template
import get_weather
import requests

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/tempmap')
def hello_project():
    req = requests.get('https://data.sparkfun.com/output/aGOE6rY5mxcxX1GNnOKq.json?page=1')
    data = req.json()
    rows=[]
    for i in range(0,20):
        lat = data[i]['latitude']
        lon = data[i]['longitude']
        tempc=data[i]['temperature']
        light=data[i]['light']
        rows.append((lat,lon,tempc,light))
    return template('tempmap', rows=rows)

@route('/templight')
def templight():
    return template('bar')

@route('/map')
def map_route():
    list = get_weather.get_weather_list()
    states = []
    reds = []
    greens = []
    blues = []
    for item in list:
        states.append(item)
        blues.append(list[item]['humidity']*2)
        reds.append(0)
        greens.append(int(list[item]['temp']-273)*5)
    return template("map", states = states, reds = reds, greens = greens, blues = blues)

@route('/sample')
def sample_route():
    list = get_weather.get_weather_list()
    i = 10
    states = ''
    colors = ''
    for item in list:
        states = states + '"' + item + '",'
        colors = colors + '' + str(i) + ','
        i = i + 4
    return template("sample",states=states,colors=colors)

@route('/data_json')
def jason():
    req=requests.get('https://data.sparkfun.com/output/pwvnLo9VnESV83OR4gan.json?')
    data = req.json()
    return template("samples",data=data)

@route('/chart1')
def charts():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.json?')
    data = req.json()
    return template("chart2",data=data)

@route('/expmap')
def expmaps():
    req=requests.get('http://data.sparkfun.com/output/aGOE6rY5mxcxX1GNnOKq.json?')
    data = req.json()
    return template("expmap",data=data)

@route('/chart2')
def piecharts():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.json?')
    data = req.json()
    return template("chart3",data=data)

@route('/area')
def area():
    return template("area")

@route('/iot')
def iot():
    return template("iot")

@route('/hello')
def hello_worlds():
    return template("hello")

@route('/project')
def projects():
    return template("project")

@route('/exp')
def exp():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.csv?')
    data = req.json()
    return template("exp",data=data)

@route('/marker')
def marker():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.json?')
    data = req.json()
    return template("marker",data=data)

@route('/bounce')
def bounce():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.json?')
    data = req.json()
    return template("bounce",data=data)

@route('/simple')
def hello_world_simple():
    return template("simple")

@route('/map')
def maps():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.json?')
    data = req.json()
    return template("map",data=data)

@route('/gmap')
def gmaps():
    req=requests.get('https://data.sparkfun.com/output/ZGgZrlDoG1uZyO8R4w0V.json?')
    data = req.json()
    return template("gmap",data=data)

@route('/weather')
def weather():
    req=requests.get('https://data.sparkfun.com/output/pwvnLo9VnESV83OR4gan.json?')
    data = req.json()
    return template("weather",data=data)

@route('/chart3')
def chart():
    return template("chart")

application = default_app()

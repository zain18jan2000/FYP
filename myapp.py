from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route('/')
def main_function():

    return render_template('index.html')

@app.route('/location',methods = ['GET','POST'])
def locations():

    dic = request.form.to_dict()
    place = dic['location']
    place = place.lower()
    try:
        img_path = os.listdir('static/'+place)
        print(place)
        case = place+place

        map_path = os.listdir('static/'+place+place)

        img_path = [place + '/' + image for image in img_path]
        map_path = [place+place+'/' + image for image in map_path]

        return render_template('location.html', img_path= img_path,map_path= map_path,lat= 24.93003937149469 ,lng = 67.11528342398769)
    except:
        return 'PLACE NOT FOUND  :('

app.run(host = '0.0.0.0')

# AIzaSyClmZ8ei6C0f10xmuuDGoifOu8zB0m5oEc


# AIzaSyAR4iCLCSwn8-1eTqcGy9KsbOsukySIDRE
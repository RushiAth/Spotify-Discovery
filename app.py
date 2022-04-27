from flask import Flask, render_template
from data import get_data
import random
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello():
    #BLACKPINK, IU, EZ Kim, Heize
    artist_list = ['41MozSoPIsD1dJM0CLPjZF', '3HqSLMAZ3g3d5poNaI7GOU', '5WJOZ5N4iegy9XdltTo8os', '5dCvSnVduaFleCnyy98JMo']
    rand = random.randint(0, len(artist_list) - 1)

    info = get_data(artist_list[rand])

    return render_template(
        'index.html',
        songName = info[0],
        artistNames = info[1],
        albumImage = info[2],
        previewURL = info[3],
        spotifyURL = info[4],
        totalArtists = len(info[1])
    )
if __name__ == '__main__':
    app.run(
        debug = True,
        host = os.getenv('IP', '0.0.0.0'),
        port = int(os.getenv('PORT', 8080))
    )

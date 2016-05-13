from torrentClient.torrents_webscraper import TorrentGetter
import flask
from flask import request
import json
import subprocess

app = flask.Flask(__name__)
torrentGetter = TorrentGetter()


@app.route('/all_torrents')
def torrent():
    res = {}
    t = torrentGetter.get_all_torrents()
    res.update({'piratebay_tv': t[0],
                'piratebay_movie': t[1],
                'kickasstorrent': t[2]})
    return json.dumps(res)

@app.route('/movies')
def movies():
    return json.dumps(torrentGetter.get_movies())

@app.route('/series')
def series():
    return json.dumps(torrentGetter.get_series())

@app.route('/add_torrent', methods=['POST'])
def add_torrent():
    req = request.json
    print('received request to add torrent')
    print(req)
    if 'magnet' in req:
        cmd = 'transmission-remote -a \'' + req['magnet'] + '\''
        subprocess.call(cmd.split())
        # print(cmd.split())
        return '', 200
    else:
        return 'no magnet send', 400

@app.route('/remove_torrent', methods=['POST'])
def remove_torrent():
    # TODO
    return 'todo'

@app.route('/status')
def status():
    # TODO
    return 'todo'

if __name__ == "__main__":
    print("app started on port 8888")
    app.run(port=8888, debug=True)

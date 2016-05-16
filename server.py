from flask import request, Flask
from flask.ext.cors import CORS
import json
from torrentClient.torrents_webscraper import TorrentGetter
from transmission_parser import TransmissionWrapper

app = Flask(__name__)
CORS(app)
torrentGetter = TorrentGetter()
transmisionWrapper = TransmissionWrapper()

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
    print(request.data)
    req = json.loads(request.data.decode())
    print(req)
    print('received request to add torrent')
    if 'magnet' in req:
        res = transmisionWrapper.add_torrent(req['magnet'])
        return json.dumps({'response': res.decode()}), 200
    else:
        return 'no magnet send', 400

@app.route('/remove_torrent', methods=['POST'])
def remove_torrent():
    req = request.json
    if 'target' in req:
        res = transmisionWrapper.remove_torrent(req['target'])
        return res, 200
    return 'no target specified', 400

@app.route('/torrents_status')
def status():
    res = transmisionWrapper.torrents_status()
    return json.dumps(res), 200

@app.route('/search', methods=['POST'])
def search():
    req = request.json
    if 'query' in req:
        res = transmisionWrapper.search(req['query'])
        return res, 200
    return 'no query specified', 400

if __name__ == "__main__":
    print("app started on port 8888")
    app.run(host='0.0.0.0', port=8888, debug=True)

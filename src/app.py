from flask import Flask, render_template, request
from spotifyconnector import SpotifyConnector
import logging

app = Flask(__name__)
spotify_connector = SpotifyConnector()

logging.basicConfig(level=logging.INFO)


@app.route('/artists/search', methods=['GET','POST'])
def search_artist():

    # The same template is used for GET and POST requests
    # the difference being that for GET requests artist_name and search_results will be set to None
    artist_name = None
    search_results = None

    # If the request was a POST then read the artist name from the form and perform a search
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        search_results = spotify_connector.search_by_artist_name(artist_name)

        # This is a hack to copy the items array into a new result_items array because jinja2 confuses it with the items() dictionary function
        search_results['artists']['result_items'] = search_results['artists']['items']

    # The same template is used for both POST and GET requests
    return render_template('artist_search.html', artist_name=artist_name, search_results=search_results)


@app.route('/artists/<artist_id>/albums', methods=['GET'])
def display_artist_albums(artist_id):

    # Read the artist ID from the request path and get their albums
    album_results = spotify_connector.get_albums_by_artist_id(artist_id)

    # This is a hack to copy the items array into a new album_items array because jinja2 confuses it with the items() dictionary function
    album_results['album_items'] = album_results['items']

    return render_template('artist_albums.html', album_results=album_results)


if __name__ == '__main__':
    app.run()

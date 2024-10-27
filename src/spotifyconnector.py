import requests
import logging
import os
from datetime import datetime
from dotenv import load_dotenv

class SpotifyConnector:
    # Token used on all the requests
    access_token = None

    # Time when the token was created
    token_created_time = None

    # Client ID and Secret
    client_id = None
    client_secret = None

    # Integer representing the time the token is valid for in seconds
    token_expiry = None

    # URL used to generate a new authentication token
    token_url = 'https://accounts.spotify.com/api/token'

    # URL used for API calls
    api_base_url = 'https://api.spotify.com/v1'
    search_path = '/search'
    albums_by_artist_path = '/artists/%s/albums'
    artist_by_album_path = '/albums/%s/artist'

    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")

    def check_token(self):

        # If the token is not created or has expired then create a new one
        if self.token_created_time is None or (datetime.now() -  self.token_created_time).total_seconds() > self.token_expiry:
            self.refresh_token()
            self.token_created_time = datetime.now()

    def refresh_token(self):
        logging.info('Refreshing authentication token')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        # POST request to generate a token using the Spotify Accounts API
        # see https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token
        response = requests.post(self.token_url, data=data, headers=headers)

        # If a token could not created then raise an exception as the application cannot work without it
        if response.status_code == 200:
            logging.info('Successfully authenticated')
            self.access_token = response.json()['access_token']
            self.token_expiry = response.json()['expires_in']
        else:
            logging.error(f"Could not authenticate {response.status_code}:")
            logging.error(response.text)
            raise Exception("Authentication failure")
    
    # Helper method to generate request headers containing the authentication token
    def build_headers_with_auth_token(self):
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        return headers


    def search_by_artist_name(self, artist_name):

        # Make sure we have a valid token
        self.check_token()

        params = {
            'q': f'artist:{artist_name}',
            'type': 'artist'
        }

        url = self.api_base_url + self.search_path

        # GET request to search by artist name
        # see https://developer.spotify.com/documentation/web-api/reference/search
        logging.info(f'Sending GET request to search artists by name: {artist_name}')
        response = requests.get(url, params=params, headers=self.build_headers_with_auth_token())

        # If the request failed for whatever reason then log the response
        if response.status_code == 200:
            json_response = response.json()
            total_results = json_response['artists']['total']
            logging.info(f'Search by artist name request successful, found {total_results} results')
            return json_response
        else:
            logging.warn(f"Could not search by artist {response.status_code}:")
            logging.warn(response.text)
            return None


    def get_albums_by_artist_id(self, artist_id):

        # Make sure we have a valid token
        self.check_token()

        params = {
            'include_groups': 'album',
        }

        url = self.api_base_url + (self.albums_by_artist_path % artist_id)

        # GET request to get albums for an artist ID
        # see https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums
        logging.info(f'Sending GET request to get artist albums for artist ID: {artist_id}')
        response = requests.get(url, params=params, headers=self.build_headers_with_auth_token())

        # If the request failed for whatever reason then log the response
        if response.status_code == 200:
            json_response = response.json()
            total_results = json_response['total']
            logging.info(f'Search by artist name request successful, found {total_results} results')
            return json_response
        else:
            logging.warn(f"Could not get album by artist {response.status_code}:")
            logging.warn(response.text)
            return None

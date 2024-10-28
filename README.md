# Spotify Web Application Task
Improve a Web Application based on the Spotify API.

The instructions below assume a Windows installation.

## Installing the tools we need

Install the following applications:
- Visual Studio Code: https://code.visualstudio.com
- Git for Windows: https://github.com/git-for-windows/git/releases/tag/v2.45.2.windows.1 (you want the one called Git-2.45.x-64-bit.exe)
- Python: https://www.python.org/downloads/
- Postman: https://www.postman.com/downloads/ (Optional)

### Making sure we have everything
First, we make sure we have everything installed that we need. In Powershell, type the following
```
git --version
python --version
```
These commands should give you a response that says something like "version 2.25.2". If instead Powershell says it can't find the command, you haven't installed Git or Python properly. Common errors include Python not being in the PATH environment variable.

### Installing Python dependencies

Create a virtual environment in the root of the project:

```
python -m venv .venv
```

Start virtual environment (if this fails, see below):

```
.venv\Scripts\Activate.ps1
```

Install Flask and Requests, which are extra tools we need to run our project

```
pip install flask
pip install requests
pip install python-dotenv
```

### If the "Start virtual environment" bit didn't work
Sometimes the execution policy prevents unsigned PowerShell scripts from running which will block venv. To work around this you can run:
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

### Starting the app
In Powershell, run the following:
```
cd src
flask run --debug
```

Now in your web browser open http://localhost:5000/artists/search and you should see the site.

## Create a Spotify developer account

To use the Spotify API you need to create an account and get a special key, so that Spotify can identify you. You can use your own Spotify account or set one up with your email. You only have to get the Client ID and Secret once.

Follow the steps in https://developer.spotify.com/documentation/web-api/tutorials/getting-started.

Make a note of your Client ID and Secret.

Copy `example.env` to `.env` and add in the actual values of the id and secret to the newly created file.

## External documentation

See https://developer.spotify.com/documentation/web-api for the Spotify API documentation.

## How to use the Postman Collection

- In Postman, create a new private Workspace
- Click on Import, select the Spotify API.postman_collection.json file
- Create a new environment called "Spotify Tests"
- Update the Body of "01 Request Access Token" with valid credentials (client_id and client_secret)
- Run "01 Request Access Token" to authenticate first, it will automatically save the authentication token in environment

## What do we start with?
We have:
- Postman set up with the Spotify API, to experiment with queries without having to write code
- A template web server written in Python + Flask, which has enough code to query artists

The template server consists of the following:
- app.py, a Python file that counts as the "start" of the code. It listens for when someone tries to access the site, and builds a web page
- spotifyconnector.py and spotifycredentials.py, which are extra files made to easily connect to the Spotify API
- A "static" folder, which contains files which should be available to every web page. This includes a CSS style file and a JS code file.
- A "templates" folder, which contains HTML files with Python templating code. This defines the contents of the web page

If you want to change how the site works, edit the .py files. If you want to change the contents of the web page, change the HTML files. If you want to change what elements on the page look like, change the CSS file. If you want to add extra functionality to the page, such as when something is clicked, change the JS file. 

## Exercises

Suggested improvements:
- Add links to Spotify on the Artists page
- Add links to Spotify on the Albums page
- Fix the broken "See tracks" functionality on the albums page
- Create an artist page using the v1/artists/{{artist_id}} API call
- Change the search functionality to include albums and tracks
- Containerise the application (create a Dockerfile) ensuring that versions of dependencies are pinned
- Investigate using a different grant_type in place of client_credentials
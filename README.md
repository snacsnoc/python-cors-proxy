# python-cors-proxy

A simple CORS proxy in Python/Django to fetch content from remote sites without a CORS policy. 

This is a fork of [fraigo/python-cors-proxy](https://github.com/fraigo/python-cors-proxy) with added *quality of life* features.

For benchmarks, see BENCHMARKS.md

## Run a web server locally

1. Install dependencies 

`pip install -r requirements.txt`

2. Set environment variables

`SECRET_KEY` Django secret key
`DJANGO_DEBUG` Django debug flag, set  to TRUE to enable. Default disabled
`ALLOWED_HOSTS` Allowed hosts string
`ALLOWED_ORIGINS` Allowed origins string

3. Start the local web server

`python3 manage.py runserver`

4. Your application will be served at http://localhost:8000/

You can modify the local port (current, `8000`) running the server with an extra parameter:

`python3 manage.py runserver 0.0.0.0:LOCALPORT` 

## Run locally using Docker

1. Install Docker Desktop

2. Run `docker-compose up` from the application folder (`docker-compose up -d` to leave it in the foreground and `docker-compose stop` to stop it)

3. Your application will be served at http://localhost:8000/

You can modify the local port (current, `8000`) changing `docker-compose.yml`

```yml
ports:
    - 'LOCALPORT:8000'
```

## Usage


You can request any URL using:

`http://your.server/?url=https://your.url/request/`

Once started your server, try for example, fetching [http://ip-api.com/json/8.8.8.8](http://ip-api.com/json/8.8.8.8):

`http://localhost:8000/?url=http://ip-api.com/json/8.8.8.8`

Sample result:

```json
{"as":"AS15169 Google LLC","city":"Mountain View","country":"United States","countryCode":"US","isp":"Level 3 Communications","lat":37.4229,"lon":-122.085,"org":"Google Inc.","query":"8.8.8.8","region":"CA","regionName":"California","status":"success","timezone":"America/Los_Angeles","zip":"94043"}
```

## Deployment to Heroku

### Install Heroku client

This command line interface (CLI) helps to do some tasks related to Heroku. 

You can install this tool following [the official guide](https://devcenter.heroku.com/articles/heroku-cli#download-and-install). 

The main steps are:

1.- For macOS, install Homebrew and run
`brew install heroku/brew/heroku`

2.- In Ubuntu/Debian based systems, install SnapCraft and run
`sudo snap install --classic heroku`

3.- For Windows, download and execute the installer.

### Create a Heroku Account 

Create an account in Heroku.com to login (https://signup.heroku.com/)


### Login into Heroku

You need an account in Heroku.com to login.

`heroku login [--interactive]`

### Register your application in Heroku

1. Manual registration:
    1. After registration, go to https://dashboard.heroku.com/
    2. Create a new application using the button [Add] (https://dashboard.heroku.com/new-app)
2. Using Heroku CLI:
    1. Run in your project:
    `heroku apps:create your-app-name`
3. Set `ALLOWED_HOSTS` in environment variables/secrets: 
    
Example:
```
ALLOWED_HOSTS = localhost,your-app-name.herokuapp.com
```

### Connect your repository with Heroku

Optionally, register your application as a python/django project:

`heroku buildpacks:set heroku/python`

Also, if you registered the application **using the web dashboard**, run this command, using the **app name** you previously registered in Heroku

`heroku git:remote -a your-app-name`

### Deploy your application

`git push heroku master`


Now your application is published at `https://your-app-name.herokuapp.com/`


URL Shortener Application
Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/AdityaSharma96/URLShortener.git
$ cd URLShortener
Create a virtual environment to install dependencies in and activate it:

$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(venv)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.
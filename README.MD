# URL Shortener Application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/rishabhrathi22/url_shortener.git
$ cd url_shortener
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/url/shorten/`.
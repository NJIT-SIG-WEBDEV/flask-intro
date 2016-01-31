## Intro to Flask

### What should I have installed to get started?

There are a few packages that need to be installed to get started:
- [virtualenv](https://virtualenv.readthedocs.org/en/latest/): Creates isolated Python environments.
- [pip](https://pip.pypa.io/en/stable/installing/): Package Manager for Python
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git): Version Control System

### Setting up the basics

Navigate to a folder you want to store this project in and then execute the following commands:

```bash
mkdir FlaskApp
cd FlaskApp
git init
touch .gitignore
touch app.py
```

So what happened there? We created a new folder in which we initialized a git repository and created a Python file that will serve as our main app. Awesome!

Open up .gitignore and add some basics in.
```bash
.DS_Store # For Mac users only
*.pyc
```
NOTE: .pyc files are Python Compiled files; when an opportunity presents itself, Python will create these binaries that help the app run faster at runtime. While they're great to have, you don't need them in your git commits.

### Setting up for the Python Flask app.

#### virtualenv

Cool, now let's get started with some Python. The first thing we have to do is create a virtual environment and have our application "source" from it:

```bash
virtualenv venv
source venv/bin/activate
```

So what happened there? We created a new virtual environment, which created a folder called `venv/`. We then set our Python app to "source" from it, meaning that moving forward, the app will look to this folder for any dependencies it requires to run. You'll know that this was successful if, at the beginning of your Terminal prompt (even before the $), you see `(venv)`.

Why did we do this? Imagine you have 50 different Python apps created over the course of 3 years. Each one uses open source dependencies that are updated every day. There's a high chance that your old apps would fall apart if they suddenly had to use the new versions of the dependenices it has installed. Virtualenv solves this by creating individual ecosystems for each application so that they continue to use the relevant versions of packages for the lifetime of that application.

The last step is to add `venv/` to our .gitignore file. We can do this by opening up the file, adding a new line at the bottom and simply typing `venv/`. A valid question here would be, "Wait, isn't `venv/` incredibly important to our app? Why would we ignore it?" We'll tackle this question shortly!

#### pip

Now, time to install packages with pip. Right now, there's only one that we have to install:

```bash
pip install Flask
```

You'll notice that a bunch of lines are printed to the console by pip. Use these in the event that there are errors - you'll have descriptive messages to debug from! 

One final task for this package is to deal with `venv/` being in our .gitignore file. If we push this to GitHub and someone else wants to see what dependencies we used, how are they supposed to figure out? We do this using a `requirements.txt` file. Go ahead and execute `pip freeze` in Terminal. As long as you still have `(venv)` set as your source, you should see a handful of requirements printed to the Terminal, along with their versions. Add them all to a `requirements.txt` file by executing the following commands:

```bash
touch requirements.txt
pip freeze > requirements.txt
```

If you open up `requirements.txt`, you'll see that it has all of those packages added to it! Now whenever you want to install those requirements to a virtual environment, you can simply create a new virtual environment and then run:

```bash
pip install -r requirements.txt
```

And just like that, we found a way to avoid uploading all of those overhead files to our GitHub repositories while still allowing other folks to play with our applications!

Once you're done, you are all set to dive into the real deal: `app.py`

#### app.py
Let's start with this: the source code that will comprise of your first Python/Flask application:
```python
from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def hello():
	return "Hello, world!"

if __name__ == "__main__":
	app.run(host="127.0.0.1")
```

Heh, yeah that's it. That's literally a Python/Flask application. Let's discuss what's happening.

- `from flask import Flask` imports the Flask class from the flask.py file that was installed in venv/ when you executed `pip install Flask`.
- `app = Flask(__name__)` instantiates the Flask application. Based on where you run it from, the __name__ variable will be different. However, when you run `python app.py` in Terminal, the name will be __main__. 
- `app.debug = True` activates Flask's awesome debug functionality, which gives in-depth tracebacks to help us debug.
- `@app.route('/', methods=['GET'])` declares a new Route for our application. In this case, it is the 'root' of the application which can be found at `http://localhost/`. A route such as 'login' would look like `http://localhost/login` in our browser URL bar. We also specify that only GET requests are allowed on this route. Any other request results in an HTTP 405 - Method Not Allowed response from the framework.
- `def hello():` sets up the function that is executed when a user visits the 'root' route. Every route must return something, the return statement being what the end user ultimately sees. Here, we're simply displaying the text "Hello, world!" without formatting it in anything like HTML or JSON. More on that later!
- `if __name__ == "__main__":` asks the program to "run" the application if the __name__ variable is __main__. This will happen in the event that the Python file is directly executed (ex: `python app.py` in Terminal). If the file is imported into another file (which may need to happen, as you'll see in the future), this is not executed. 

Let's save this Web Application and head to Terminal, where we'll run it for the first time. Type in `python app.py` in the command line. Make sure that:
- You're in the right folder.
- Your `(venv)` is active.

If all goes well, you'll see something similar to this line: `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`. Go to your browser and visit `http://localhost:5000`. You'll be greeted by your own application!

Let's push it a bit further. Keep your application running and open up a new Terminal window. Enter the following commands:
```bash
curl -X GET "http://localhost:5000"
curl -X POST "http://localhost:5000"
```

How does your application react? Is it doing what it's supposed to? You can modify your cURL request to include headers by including the `-i` flag right after the `curl` keyword.

And there you have it - you've set up your first Web Service! The purpose of this Web Services is to greet visitors with "Hello, world!". Great work!

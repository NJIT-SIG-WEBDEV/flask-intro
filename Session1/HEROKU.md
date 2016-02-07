## Deploying to Heroku

### But first, a new route...
Hey - congrats! You made your first Python / Flask app. Before we get ready to learn Heroku, let's put together just one more route.

Go ahead and open up `app.py` and start a new route below our root route. Let's try adding this line:

```python
@app.route('/<var>', methods=['GET'])
```

Cool, so this looks a bit different. Consider a site like Facebook - over 1 billion users per day. They certainly don't hard code any of their users' usernames as routes. Instead, they use `variable` routes like this. The variable route takes WHATEVER the user puts there and passes it into the route's associated function as a parameter, allowing the logic to dictate what the user sees. Consider:

```
http://www.facebook.com/jayrav13
```

Facebook's logic probably takes jayrav13, queries it, gets my data and passes it to the client. Pretty straightforward, right?

Let's finish out that route:

```python
@app.route('/<var>', methods=['GET'])
def second(var):
	return var 
```

This is incredibly similar to our root route, but go ahead and execute `python app.py` to see what happens. You'll notice that whatever you add after the slash is displayed on the screen.

Sweet, now we have two routes! Time to deploy!

### Heroku
So what is [Heroku](https://www.heroku.com)? Instead of either renting shared hosting or setting up a virtual private server on the cloud, the members of the tech community are electing to use cloud computing platforms that take care of a lot of the hectic work of managing a server, including security and scalability. Services like this provide storage space, cloud databases and many more services. Instead of writing them yourself, you can pick and choose them and integrate them directly into your app, truly giving developers time to focus on building cool things.

Along with many paid tiers, Heroku offers a ton of unpaid services. Here's the catch though - a service like Heroku is going to be potentially unstable for non-paying customers. Further, you won't have 100% uptime. For example, Heroku only allows you to have a web app up that will be used for less than 18 out of the 24 hours in a day. If your app exceeds that time limit, you may experience extended downtime. Also, versions of MySQL allow a maximum of 1 database and 10,000 rows across all tables in that database.

But for the purpose of pushing something to a world-facing environment (personal projects, hacks, etc), this is absolutely perfect! With a simple command, we can get our app launched. Let's get started!

#### Prepare
Let's start by getting the basics out of the way. Make sure you have your virtualenv activated and execute the following:
```bash
pip install gunicorn
```

[Gunicorn](http://gunicorn.org/) is a web server that helps get Python apps up and running. Once installed, execute the following so that our requirements.txt file has it available as well:
```bash
pip freeze > requirements.txt
```

Great. Now that we have the web server available, let's take a second to talk about how Heroku actually let's us push projects. Heroku has a Command Line Interface that let's you do everything you need. Here's a ton of information on how to install it: https://devcenter.heroku.com/categories/command-line

(Note: Using the CLI will, of course, require you to have an account with Heroku. Don't forget to sign up!)

Once you have the CLI installed and have created a Heroku account, you can use the `heroku login` command to get squared away and ready to deploy your app.

So are we ready to deploy yet? Almost! One last thing we need to do is make sure that our project has git initialized in it. This tutorial specifically will NOT already have this done, so we'll have to move our project to a new folder to do this. Once we're in a clean, non-git folder, execute the following commands:
```bash
git init
touch .gitignore
```

The reason we created a git repository is because Heroku literally acts like a repo that you can "push" to. It makes it incredibly easy to deploy projects, no different than pushing to GitHub.

Phew - ok awesome, now let's get to Heroku:

```bash
heroku create jrfirstapp
```
If all went well, head over to [Heroku's Dashboard](https://dashboard.heroku.com/apps) and you should see that the new app has been created! Woo!

Now when you execute `git status`, you'll notice that `venv/` is still a part of this folder. Head over to your `.gitignore` file and add `venv/` to it. Heroku is awesome - it will recognize `requirements.txt` and install all of your dependencies for you, so you don't have to include `venv/` at all!

Once you're ready, push:

```bash
git add .
git commit -m "Initial Commit"
git push heroku master
```

Whoa whoa, how did `heroku` end up being a remote repository? This was done automatically upon executing `heroku create...`. Execute `git remote -v` to see it listed! You can still add GitHub as a remote under another name, most commonly `origin`.

And now, best part - execute `heroku open` and you should see your "Hello, world!" application staring you down! [Check mine out!](https://jrfirstapp.herokuapp.com/) Of course, we have to make sure our variable route is working too - give it a try.

I'll admit, even while writing this I realized Heroku can appear to be a roller coaster from the "outside", but once you're comfortable, you'll notice that this is easier than using shared hosting and VPS by multiple orders of magnitude, especially for hacks and quick projects.

Even more curious about getting quick projects on the web? Check out [ngrok](https://ngrok.com/) for another option. This one is not a "permenant" one like Heroku, but it does the trick for testing.

Congrats - you've deployed a project! Next we'll talk about Database Connectivity and migrations. Hint: you'll never type "CREATE TABLE..." ever again :).

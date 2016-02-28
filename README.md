## Special Interest Group - Web Development, Backend

The purpose of this repo is to host introductory material on Backend Web Development, specifically demonstrated through Python/Flask framework. Feel free to drop me a line at any time with questions or comments!

- Session 0: Intro to Web Development, Flask
- Session 1: Intro to Heroku
- Session 2: Make a Link Shortener!

## Getting Started with Ubuntu
### Setup Your Development Environment

To get started with your development environment, first consider the operating system that you have installed. Many folks begin developing on a Windows PC, but this sometimes presents a challenge. First off, there is NO issue with working on Windows. However, there are a few drawbacks compared to developing on a UNIX-based system (Ubuntu, Linux, Mac OS):

- There is a lot more developer support for UNIX based systems.
- There is more software that is made available through UNIX based systems.
- Most documentation is available for UNIX based systems.
- Many UNIX based systems come with package installers that make installing software super easy:
 - Ubuntu: apt-get
 - Linux: yum
 - Mac OS: brew [independently developed, search "Homebrew"]

I am sure there is room for argument for everything above, but at the end of the day learning to use something like Ubuntu or Linux will put you one step ahead as most systems are built off of them. So if you have a Windows PC, does that put you at a disadvantage? Absolutely not! Since these are Open Source Operating Systems, you can very easily install it on your Windows PC and have it up and running in no time!

The two methods to install Ubuntu on your system are:
- Dual Boot Installation
 - Allows the resources of your PC to be dedicated to any one OS at any given time.
 - Positive performance impact.
 - Have to restart computer to enter other OS.
- Virtual Box Installation [my recommendation]
 - Allows you to run both OS's at the same time.
 - May have performance issues if you have very little RAM in your computer (< 2 GB)

To make this work, you'll want to install [Virtual Box](https://www.virtualbox.org/wiki/Downloads). An Oracle product, Virtual Box allows you to install Ubuntu onto your Windows PC.

You will also have to download [Ubuntu](http://www.ubuntu.com/download/desktop). The download will be in .iso format.

A sample walkthrough of how to go about this is [available here](http://www.psychocats.net/ubuntu/virtualbox). There are definitely more updated versions of this, a simple Google search should lead you to one!

Once installed, definitely make sure that your Ubuntu instance can connect to the internet. I have seen many cases where secure networks (i.e. RUWireless Secure, NJITsecure) don't work on Virtual Machines. In this case, you may want to consider using a hot spot with your phone or some similar alternate. 

### Terminal
The Command Line is the most important tool a developer can learn! Commands that are used constantly include, but are not limited to: `cd`, `touch`, `mkdir`, `rm`, `ls` and more.

New to the Command Line? Check out [Code Academy's Learn the Command Line course](https://www.codecademy.com/learn/learn-the-command-line). 

### Installing LAMP

This is where you'll almost instantly start seeing how much easier it is to use Ubuntu for development! Get started by installing LAMP - there is a really awesome guide on this by Digital Ocean, [available here](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu).

Once this is good to go, you should be able to access your MySQL database with the command:
```bash
mysql -u root -p # -p is only if you have a password set
```

### Installing MongoDB
*Windows/Mac users*

To install MongoDB, you'll need to grab MongoDB [here](https://www.mongodb.org/downloads#production). For Windows users, just grab the Windows 32-bit version.

#####Windows users:
Once you install MongoDB, you'll need to to add two folders into the directory. This process may change depending on your OS. Open Command Prompt and navigate to the MongoDB directory inside the Program Files folder or the folder you installed it. Then follow the process below.:
```
cd Server\3.2
mkdir data\db
cd bin
mongod
```

#####Mac Users
[Installing MongoDB on OS X](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition-manually)

*Linux Users*

[Installing MongoDB on Ubuntu](https://docs.mongodb.org/v3.0/tutorial/install-mongodb-on-ubuntu/)

If you see 'waiting for connection' when you start the mongod process, then you're good to go! mongod starts the Mongo server. You'll have to keep it running while you use MongoDB. To begin playing around with MongoDB, while staying in the directory, type 'mongo' and hit enter.

Here are some resources to learn how to use MongoDB.

[MongoDB Official Documentation](https://docs.mongodb.org/manual/core/introduction/)

[Tutsplus Getting Started with MongoDB Part 1](http://code.tutsplus.com/tutorials/getting-started-with-mongodb-part-1--net-22879)

### NodeJS
Install NodeJS (1st answer): http://askubuntu.com/questions/594656/how-to-install-the-latest-versions-of-nodejs-and-npm-for-ubuntu-14-04-lts

See if npm is installed.  If not; 'sudo apt-get npm'

ExpressJS Hello World: http://expressjs.com/en/starter/hello-world.html

http://expressjs.com/en/starter/installing.html

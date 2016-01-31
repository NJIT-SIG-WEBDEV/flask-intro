## Intro to Web Development

### Why learn Web?
Web Development, Applications and Services are some of the most important areas of growth for the future of the Internet. Granted, this begs the question - what exactly is Web?

The Web can include, but is not limited to:
- Websites: both static and dynamic, both visually involved and server-side intensive.
- Web Applications: from enterprise to social, from home built to industry driven. 
- Web Services: the broader term which references delivery of data from a web server to web-driven clients, including websites, mobile devices, IoT products, wearables and more. These are generally enabled by cloud services.

That escalated quickly, no?

### So where the heck does one start?
While the above is a vortex of cliche sounding buzz words, there's truth to the breadth of work being done in the Web space. Let's start small though. What has the evolution of the Web looked like?

Eleven years ago when Facebook launched, they literally wrote .php files and put them up on a Web Server which let users interact with their server. You can still, to this day, figure out your User ID and visit https://www.facebook.com/profile.php?id=YOURUSERID and you'll be taken to your Facebook profile. There's absolutely nothing wrong with this approach. In fact, I recommend you trying it. [That's how I started](https://github.com/jayrav13/cs431-chat). But as far as industry standards go, it's consdered Archaen. In fact, shortly after Facebook grew in popularity, the notion of Web Frameworks was introduced.

- Popular Web Languages:
 - Python
 - PHP
 - Ruby
 - JavaScript / NodeJS
- Frameworks atop these technologies:
 - Python: Flask, Django
 - PHP: Silex, Lumen, CakePHP, Laravel
 - Ruby: Sinatra, Rails
 - JS : ExpressJS

With Web Frameworks, you're empowered to build cool stuff fast and have almost all the tools you need built right in. From database connectivity to email integration and more, the most popular frameworks make it super easy to get started right out of the gate. We're going to start of by learning Python's Flask microframework. The reason for this is simple - it's incredibly easy to learn, and even those with limited Python experience can pick it up. Further, it doesn't come with all of the bells and whistles that Python's Django framework does, allowing us to make incremental progress in understanding how those major frameworks work.

Some other benefits:
- Incredibly lightweight, which means it is fast.
- pip, Python's Package Management System, is littered with awesome packages to help you build out awesome Web Services.
- Deployments using Heroku can make your Web Services available to the public in minutes. It's as easy as `git push heroku master` (more on that later!)
- Not only is it fast, but it's also fast to set up, making it the ideal framework for hackathons and personal projects alike.

Awesome - let's get started!

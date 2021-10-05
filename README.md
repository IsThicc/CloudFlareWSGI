# CloudFlareWSGI

A simple module to get a client's IP address when behind a CloudFlare proxy.

## Installation 

You can install this module using PIP. Currently, we have not published 
this to PyPi, and have no plans to in the future.

`pip install git+https://github.com/IsThicc/CloudFlareWSGI@stable`

*Side note: In order to run the test script, you will need to install Flask.*

## Usage 

This middleware has only been tested using Flask version 1.0.1, though, most versions 
should work because this middleware is rather simple.

Below is an example using Flask:

```python
from flask import Flask 
from cloudflare_wsgi import CloudFlareMiddleware

app = Flask(__name__)
app.wsgi_app = CloudFlareMiddleware(app.wsgi_app)

# Continue with your Flask application below. You should 
# now see the real client IP in flask.request.request_addr 
# when a client requests your site.
```

## Contributors

- [Joshua Sing](https://github.com/JoshuaSing)
- [Mrmagicpie](https://github.com/Mrmagicpie)

## Contributing

Feel free to fork this repo and make any edits you think would be beneficial. 
An IsThicc staff member will review your pull request and approve or deny it.

### Please note:

We reserve the right to reject any pull request or edits without reason or 
warning. When editing any IsThicc source code, you waive all rights over the 
code you contribute. Any attempt to claim the code as your own will be met with 
consequences to our fullest extent.

All data in this repository is owned by [IsThicc](https://isthicc.dev/). For 
further Legal and Copyright concerns or information, please email our Management 
(contact information can be found on our website).

<p align="center">Copyright (c) 2020-2021 IsThicc Software</p>

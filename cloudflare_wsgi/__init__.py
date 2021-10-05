
__license__ = 'Apache Version 2.0'
__version__ = "1.0.0"
__authors__ = ["Mrmagicpie: <pie@mrmagicpie.xyz>"]

class CloudFlareMiddleware(object):
    def __init__(self, wsgi_app):
        self._wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # All headers are prefixed with `HTTP`, and the
        # header CloudFlare provides (at time of writing)
        # is `Cf-Connecting-Ip`.
        cf_ip = environ.get("HTTP_CF_CONNECTING_IP")
        if cf_ip is not None:
            environ['REMOTE_ADDR'] = cf_ip
        return self._wsgi_app(environ, start_response)

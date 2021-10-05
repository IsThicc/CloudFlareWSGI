
from flask import Flask, request, wrappers
from cloudflare_wsgi import CloudFlareMiddleware

app = Flask(__name__)
app.wsgi_app = CloudFlareMiddleware(app.wsgi_app)

@app.route("/", methods=["GET"])
def index_get():
    return f"ok; {request.remote_addr}", 200

with app.test_client() as client:
    resp: wrappers.Response = client.get(
        "/", headers={"cf-connecting-ip": "10.10.10.10"}
    )
    print(resp.data)

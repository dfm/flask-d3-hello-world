import json

import flask
import numpy as np


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=10):
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 2 * np.random.randn(ndata)
    return json.dumps([{"x": x[i], "y": y[i]} for i in range(ndata)])


if __name__ == "__main__":
    import os
    port = 4000
    os.system("open http://localhost:{0}".format(port))
    app.debug = True
    app.run(port=port)

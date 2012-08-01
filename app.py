"""
This file is part of the flask+d3 Hello World project.
"""
import json
import flask
import numpy as np

# @dfm what does this next line do?
app = flask.Flask(__name__)

# @dfm what is the @app.route() doing?
@app.route("/")
def index():
    """
    @dfm:  What does this do?
    """
    return flask.render_template("index.html")

@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ndata randomly made data points.
    """
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    return json.dumps([{"x": x[i], "y": y[i], "area": A[i]} for i in range(ndata)])

def main():
    """
    This function opens port 4000 and does what?  @dfm??
    """
    port = 4000
    os.system("open http://localhost:{0}".format(port))
    app.debug = True
    app.run(port=port)

if __name__ == "__main__":
    import os
    main()

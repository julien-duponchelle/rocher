"""
This demonstrates a simple Flask app with
the Monaco editor.

To run this sample, you need to install flask:
    pip install flask

Then run the app:
    python app.py

Then open your browser to http://localhost:5000
"""

from flask import Flask, Blueprint
import rocher

app = Flask(__name__)

# Serve the static files from the Monaco editor
blueprint = Blueprint(
    "monaco", __name__, static_url_path="/static/vs", static_folder=rocher.path()
)
app.register_blueprint(blueprint)


@app.route("/")
def hello():
    return """
    <html>
    <body>
    <h1>Flask Sample</h1>
    The static files are served from the <code>static</code> folder.
    <br>
    <a href="/static/hello.txt">Hello.txt</a>
    <br>
    Monaco editor is loaded via /static/vs

    <div id="container" style="width:800px;height:600px;border:1px solid grey"></div>

    <script src="/static/vs/loader.js"></script>
    <script>
        require.config({ paths: { vs: '/static/vs' } });
        require(['vs/editor/editor.main'], function () {
				var editor = monaco.editor.create(document.getElementById('container'), {
					value: ['def hello():', '\\tprint("World")'].join('\\n'),
					language: 'python'
				});
			});
    </script>

    </body>
    </html>
"""

if __name__ == "__main__":
    app.run()

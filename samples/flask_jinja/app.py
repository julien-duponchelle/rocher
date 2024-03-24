"""
This demonstrates a simple Flask app with
the Monaco editor.

To run this sample, you need to install flask:
    pip install flask

Then run the app:
    python app.py

Then open your browser to http://localhost:5000
"""

from flask import Flask, render_template, request

import rocher.flask

app = Flask(__name__)

# Register the editor with the Flask app
# and expose the rocher_editor function to Jinja templates
rocher.flask.editor_register(app)

# Read the source code of this file to highlight it in the editor
with open(__file__) as f:
    source_code = f.read()

@app.route("/")
def index():
    return render_template("index.html.j2", source_code=source_code)

@app.route("/colorize")
def colorize():
    return render_template("colorize.html.j2", source_code=source_code)

@app.route("/upper", methods=["POST"])
def upper():
    if request.json is None:
        return "No JSON data received", 400
    if "source_code" not in request.json:
        return "No source_code in JSON data", 400
    return {
        "source_code": request.json["source_code"].upper()
    }
    

if __name__ == "__main__":
    app.run(debug=True)

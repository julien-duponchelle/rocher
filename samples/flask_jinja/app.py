"""
This demonstrates a simple Flask app with
the Monaco editor.

To run this sample, you need to install flask:
    pip install flask

Then run the app:
    python app.py

Then open your browser to http://localhost:5000
"""

from flask import Flask, render_template
import rocher.flask

app = Flask(__name__)

# Register the editor with the Flask app
# and expose the rocher_editor function to Jinja templates
rocher.flask.editor_register(app)

# Read the source code of this file to highlight it in the editor
with open(__file__) as f:
    source_code = f.read()

@app.route("/")
def hello():
    return render_template("index.html.j2", source_code=source_code)


if __name__ == "__main__":
    app.run(debug=True)

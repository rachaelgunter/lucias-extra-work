from flask import Flask, render_template
import jinja2 

#  import from day care csv file

app = Flask(__name__)

# app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def start():
    """goes to homepage"""

    return render_template("homepage.html")

@app.route("/info")
def show_child_info():
    "returns the results of the search"

    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
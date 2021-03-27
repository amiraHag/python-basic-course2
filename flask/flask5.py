# ------------------------------------
# -- Flask => Jinja Template Engine --
# ------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage4.html", title="Homepage")

@skills_app.route("/about")
def about():
  return render_template("about4.html", title="About Us")

@skills_app.route("/add")
def addpage():
  return render_template("add.html", title="Add")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)

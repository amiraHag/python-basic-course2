# ------------------------------------
# -- Flask => Jinja Template Engine --
# ------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage3.html", title="Homepage")

@skills_app.route("/about")
def about():
  return render_template("about3.html", title="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)

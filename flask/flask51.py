# --------------------------------------------
# -- Flask => Advanced Css Task Using Jinja --
# --------------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage41.html",
                          title="Homepage",
                          custom_css="home")
@skills_app.route("/add")
def add():
  return render_template("add1.html",
                          title="Add Skill",
                          custom_css="add")

@skills_app.route("/about")
def about():
  return render_template("about41.html", title="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)

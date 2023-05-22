from flask import Flask, render_template, url_for, request
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
@app.route("/<username>", methods=['GET'])
def hello_world_username(username=None):
    return render_template("./index.html", name=username)

@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    try:
      print(request.form['email'], request.form['passwords'])
      return render_template("./welcome.html", form=request.form)
    except BadRequestKeyError as KeyError:
      return render_template("./error.html", error=KeyError)
  else:
    return render_template("./login.html")

@app.route('/upload', methods=['GET' , 'POST'])
def upload_file():
  if request.method == 'POST':
    if request.files:
      f = request.files['file']
      f.save(f'./static/{secure_filename(f.filename)}')
    return render_template("./fileupload.html", msg="file has been uploaded")
  else:
    return render_template("./fileupload.html")

from flask import Flask, render_template, request
from controller import reader_controller as rc

app = Flask(__name__, template_folder="views")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", context=rc.dataHome())

@app.route("/detail/file/<filename>", methods=['GET'])
def detail(filename):
    return render_template("index.html", context=rc.readSingleFile(filename))

@app.route("/detail/<folder>/<file>", methods=["GET"])
def get_by_folder(folder, file):
    return render_template("index.html", context=rc.readFileInFolder(folder, file))

@app.route("/search", methods=["GET"])
def search():
    return render_template("index.html", context=rc.search(request.args.get("query")))


app.run(debug=False, port=4000)
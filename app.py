from flask import Flask, render_template
from core import MarkdownReader
import os

doc_path = "./documents"
app = Flask(__name__, template_folder="views")
mr = MarkdownReader()
list_file = mr.listDocumments(doc_path)
file_list = mr.listData(doc_path)

@app.route("/", methods=["GET"])
def home():

    file_init = ""
    
    if len(file_list) > 0:
        if file_list[0]['type'] == "folder":
            file_init = os.path.join(doc_path, file_list[0]['name'], file_list[0]['file'][0])
        else:
            file_init = os.path.join(doc_path, file_list[0]['name'])
        
    context = {
        'file_init': mr.readMarkdown(file_init),
        'headline_init': mr.getHeadline(file_init),
        'data': file_list
    }

    return render_template("index.html", context=context)

@app.route("/detail/file/<filename>", methods=['GET'])
def detail(filename):

    file = ""
    headline = []

    if os.path.exists(os.path.join(doc_path, filename)):
        file = mr.readMarkdown(os.path.join(doc_path, filename))
        headline = mr.getHeadline(os.path.join(doc_path, filename))

    context = {
        'file': list_file,
        'file_init': file,
        'headline_init': headline,
        'data': file_list,
        'title': filename.split(".")[0]
    }

    return render_template("index.html", context=context)

@app.route("/detail/<folder>/<file>", methods=["GET"])
def get_by_folder(folder, file):
    file_read = ""
    headline = []

    if os.path.exists(os.path.join(doc_path, folder, file)):
        file_read = mr.readMarkdown(os.path.join(doc_path, folder, file))
        headline = mr.getHeadline(os.path.join(doc_path, folder, file))

    context = {
        'file': list_file,
        'file_init': file_read,
        'headline_init': headline,
        'data': file_list,
        'title': file.split(".")[0]
    }
    return render_template("index.html", context=context)

app.run(debug=False, port=4000)
from flask import Flask, render_template
from core import MarkdownReader
import os

doc_path = "./documents"
app = Flask(__name__)
mr = MarkdownReader()
list_file = mr.listDocumments(doc_path)

@app.route("/", methods=["GET"])
def home():

    file_init = ""
    headline = ""
    
    if len(list_file) > 0:
        if os.path.exists(os.path.join(doc_path, list_file[0])):
            file_init = mr.readMarkdown(os.path.join(doc_path, list_file[0]))
            headline = mr.getHeadline(os.path.join(doc_path, list_file[0]))

    context = {
        'file': list_file,
        'file_init': file_init,
        'headline_init': headline
    }

    return render_template("index.html", context=context)

@app.route("/detail/<filename>", methods=['GET'])
def detail(filename):

    file = ""
    headline = ""

    if os.path.exists(os.path.join(doc_path, filename)):
        file = mr.readMarkdown(os.path.join(doc_path, filename))
        headline = mr.getHeadline(os.path.join(doc_path, filename))

    context = {
        'file': list_file,
        'file_init': file,
        'headline_init': headline
    }

    return render_template("index.html", context=context)

app.run(debug=False, port=4000)
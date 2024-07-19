from flask import Flask, render_template, request
from utils.main import Model_handler
import os, time


app = Flask(__name__, static_url_path="", static_folder="static")
model = Model_handler()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join("./server/static/received", f.filename))
        model.generate(
            input_file=f"server/static/received/{f.filename}",
            output_dir="server/static/generated/",
        )
        time.sleep(2)
        return "successful"
    else:
        return render_template("index.html")


app.run("0.0.0.0", 3002)

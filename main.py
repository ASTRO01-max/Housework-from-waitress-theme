from wsgiref.simple_server import make_server
from app import Frameworkapp

app = Frameworkapp()

@app.route("/muhammadyusuf")
def muhammadyusuf(request, response):
    response.text = "yoshi: 16, yili: 2008"

from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route("/home")
def home():
    text = "<h2>Hi you are in the home page!</h2>"
    return text

@app.route("/about")
def about():
    text2 = "<h2>This page is localhost page for waitress theme!</h2>"
    return text2

@app.route("/nodir")
def nodir():
    img_tag = '<img src="/nodir/image" alt="Nodir rasmi" width="300"><br>'

    info = """
        <h2>Sagatov Nodir</h2>
        <p>
            <span style="font-size: 18px;">Age: 17 da</span><br>
            <span style="font-size: 18px;">Hobby: Football</span><br>
            <span style="font-size: 18px;">Main task: Studying at school</span><br>
            <span style="font-size: 18px;">Zodiac sign: Unknown</span><br>
        </p>
        """
    return img_tag + info

@app.route("/nodir/image")
def nodir_image():
    try:
        image_path = r"C:\Users\hp\Desktop\download.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)

@app.route("/bobur")
def bobur():
    img_tag2 = '<img src="/bobur/image" alt="Bobur rasmi" width="300"><br>'

    info2 = """
        <h2>Inomov Bobur</h2>
        <p>
            <span style="font-size: 18px;">Age: 17 </span><br>
            <span style="font-size: 18px;">Interest: Football</span><br>
            <span style="font-size: 18px;">Favorite profession: Programming</span><br>
            <span style="font-size: 18px;">Hobby: Playing Basketball</span><br>
            <span style="font-size: 18px;">Job: Trading and Programming</span><br>
            <span style="font-size: 18px;">Main task: Studying at school</span><br>
            <span style="font-size: 18px;">Free time: Reading books</span><br>
        </p>
        """
    return img_tag2 + info2

@app.route("/bobur/image")
def bobur_image():
    try:
        image_path = r"C:\Users\hp\Desktop\bobour.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)

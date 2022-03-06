from flask import Flask, request, redirect, render_template
import validators
from modules import db
app = Flask(__name__)
app.config.update(
    SECRET_KEY='123435467443',
    SESSION_TYPE='filesystem',
)
servername = "http://localhost:8080/" #Own URL or serverip
database = db.url_model()

@app.route('/', methods= ["POST","GET"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if validators.url(url):
            try:
                short = database.create_short_from_long(url)
                message = f"URL Shortened. You can reach the URL via: <a href='{servername}{short}'>{servername}{short}</a>"
                return render_template("message.tpl", title="URL Shortened", message=message)
            except db.UrlExistsError:
                message="URL already exists in Database" 
                return render_template("message.tpl", title="URL Shortened", message=message)
        else:
            message="URL is invalid" 
            return render_template("message.tpl", title="URL Shortened", message=message)
    else:
        return render_template("index.tpl", title="URL Shortener")
@app.route("/<short>", methods=["GET","POST"])
def redirect_short(short):
    return redirect(database.get_long_from_short(short))

@app.route("/all_urls", methods=["POST","GET"])
def all_urls():
    if request.method == "POST":
        if database.delete_row(request.form.get("delete")):
            return render_template("urls.tpl",title="All URLS", urls=database.get_all_db_rows(),message="Entry deleted")
        else:
            return render_template("urls.tpl",title="All URLS", urls=database.get_all_db_rows(),message="Error deleting entry")
    else:
        return render_template("urls.tpl",title="All URLS", urls=database.get_all_db_rows())

if __name__ == "__main__":
    app.run("0.0.0.0", 8080,debug=True)
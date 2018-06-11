from db import *
from flask import Flask , request,render_template,redirect
from helper import *

app = Flask(__name__)


@app.route("/getshort",methods=["POST"])
def short_url():
    if request.method == 'POST':
        raw_url = request.form['url']
        short =  get_short_url(raw_url,request.host)
        return redirect('/')

@app.route("/getraw",methods=["POST"])
def raw_url():
    if request.method == 'POST':
        short_url = request.form['url']
        url = get_raw_url(short_url)
        return  url

@app.route("/")
def get_all():
    url_list =  get_all_url()
    return render_template('home.html',url_list = url_list)

@app.route("/<code>")
def redirect_to_url(code):
    if code != None:
        url = get_raw_url(code,request.host)
        return redirect(url)

@app.route("/delete",methods=["POST"])
def del_url():
    if request.method == 'POST':
        url = request.form['url']
        del_short_url(url)
        return  redirect('/')

if __name__ == '__main__':
    init_db('urls.db')
    app.run(debug=True)

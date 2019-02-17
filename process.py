from flask import Flask, render_template, request
from werkzeug import secure_filename
from sentiment_analysis import sentiment_main
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["UPLOAD_FOLDER"] = 'file_upload/'

@app.route('/upload')
def upload_file():
	return render_template('form.html')
	
@app.route('/uploader', methods = ['POST'])
def upload():
	f = request.files["file1"]
	if f.filename == '':
		return redirect(request.url)
	fi = open(f.filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
	sentiment_main(fi, "static/img" , 10)
	#return 'file uploaded successfully'
	return render_template("show.html")

if __name__ == '__main__':
	app.run(debug = True)
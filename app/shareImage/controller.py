from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
# from flask.ext.uploads import delete, init, save, Upload

mod = Blueprint('shareImage', __name__)

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask import send_from_directory

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
STORAGE_FOLDER = 'http://localhost/i/'
UPLOAD_FOLDER = '/tmp/upload'

# mod.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# mod.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@mod.route('/test')
def index():
    return render_template('shareImage/index.html')

@mod.route('/i/<filename>')
def uploaded_file(filename):
    return render_template('shareImage/image.html', path=str(STORAGE_FOLDER + filename))
    # return send_from_directory(UPLOAD_FOLDER, filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@mod.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('.uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
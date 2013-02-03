from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
# from flask.ext.uploads import delete, init, save, Upload

mod = Blueprint('shareImage', __name__)

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask import send_from_directory
import hashlib
import base64
import hmac
import time

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
STORAGE_FOLDER = 'http://localhost/i/'
UPLOAD_FOLDER = '/tmp/upload'

# mod.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# mod.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def getImageJson(filename):
    imagePath = str(STORAGE_FOLDER + filename)

    upload = {
        'image' : {},
        'links' : {
            'original': imagePath
        }
    }
    return upload

@mod.route('/test')
def index():
    pass

@mod.route('/<filename>')
def uploaded_file(filename):
    return render_template('shareImage/image.html', path=str(STORAGE_FOLDER + filename))
    # return send_from_directory(UPLOAD_FOLDER, filename)

@mod.route('/<filename>/json')
def uploaded_file_json(filename):
    return jsonify(upload = getImageJson(filename))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@mod.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        apikey = request.form['apikey']
        if(apikey == 'KEY_123'):
            file = request.files['file']
            if file and allowed_file(file.filename):
                name = secure_filename(generateFileName())
                file.save(os.path.join(UPLOAD_FOLDER, name))
                return redirect(url_for('.uploaded_file', filename=name))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
         <input type=text name="apikey" value="">
    </form>
    '''

def generateFileName():
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return base64.b64encode(hash.hexdigest())[:10]
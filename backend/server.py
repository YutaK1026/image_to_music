# render_template：参照するテンプレートを指定
# jsonify：json出力
from flask import Flask, render_template, jsonify, request, make_response

# CORS：Ajax通信するためのライブラリ
from flask_restful import Api, Resource
from flask_cors import CORS 
from random import *
from PIL import Image
from pathlib import Path
from io import BytesIO
import base64
#import ImageToMusic

# static_folder：vueでビルドした静的ファイルのパスを指定
# template_folder：vueでビルドしたindex.htmlのパスを指定
app = Flask(__name__, static_folder = "./../frontend/dist/static", template_folder="./../frontend/dist")

#日本語
app.config['JSON_AS_ASCII'] = False
#CORS=Ajaxで安全に通信するための規約
api = Api(app)
CORS(app)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# 任意のリクエストを受け取った時、index.htmlを参照
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def index(path):
    return render_template("index.html")

@app.route('/classification', methods=['POST'])



def uploadImage():
    if request.method == 'POST':
        base64_png =  request.form['image']
        code = base64.b64decode(base64_png.split(',')[1]) 
        image_decoded = Image.open(BytesIO(code))
        image_decoded.save(Path(app.config['UPLOAD_FOLDER']) / 'image.png')

        img = Image.open("./uploads/image.png")
        img_g = img.convert(mode = "1")
        buffered = BytesIO()
        img_g.save(buffered, format="png")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('ascii')

        return jsonify({'response_data':"data:image/png;base64,"+img_base64})
    else: 
        return make_response(jsonify({'result': 'invalid method'}), 400)

# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
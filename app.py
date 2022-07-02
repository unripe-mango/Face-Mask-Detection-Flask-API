from flask import Flask,jsonify,request,render_template,send_from_directory
from source.utils import draw_rectangles, read_image, prepare_image
from source.source import detect_faces_with_ssd, run_model
from keras.models import load_model
from config import *
import numpy as np 
import cv2
import os

os.environ['CUDA_VISIBLE_DEVICES'] = "0"
app = Flask(__name__, static_folder='static',)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = os.path.basename('uploads')

model5 = load_model(os.getcwd() +'/models/' + MODEL_NAME)


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    image = read_image(file)
    faces = run_model(image, model5)
    return jsonify(detections = faces)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    image = read_image(file)
    faces = run_model(image, model5)
    num_faces, image = draw_rectangles(image, faces)
    to_send = prepare_image(image)
    print(faces)
    return render_template('index.html', face_detected=len(faces)>0, num_faces=len(faces), image_to_show=to_send, init=True)

if __name__ == '__main__':
    app.run(debug = False)

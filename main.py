from script import url_to_image, get_dominant_color, get_hex_code
from flask import Flask, redirect, url_for, request, jsonify
from PIL import Image
import base64
from io import BytesIO
import requests
from sklearn.cluster import KMeans
from collections import Counter
import cv2
import urllib.request as ur
import numpy as np

app = Flask(__name__)

@app.route("/send-image/<path:url>")
def getapiview(url):
    
    url = url.replace(' ', '%20')
    img = url_to_image(url)

    x,y,a,b = 0,0,1000,50
    crop_img = img[y:y+b, x:x+a]

    colours = get_dominant_color(img)
    dom_code = get_hex_code(colours)

    colours = get_dominant_color(crop_img)
    border_code = get_hex_code(colours)

    resp = {
            'logo_border': border_code,
            'dominant_color': dom_code
    }
    return jsonify(resp)



if __name__ == "__main__":
    app.run(debug=True)


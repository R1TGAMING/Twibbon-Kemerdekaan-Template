from flask import Flask
from flask import *
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('main.html')

@app.route("/get", methods= ["POST"])
def receive() :
    if request.method == "POST" :
        f = request.files['file']
        img_req = Image.open(f).copy().convert("RGBA")
        img_twibbon = Image.open("./static/ImagesTwibbon/twibbon1.png").copy().convert("RGBA")
        img_new = Image.new("RGBA", (img_twibbon.width, img_twibbon.height)).copy()

        resize = img_req.resize((int(img_new.width), int(img_new.height)))
        
        img_new.paste(resize, (0, 0), resize)
        img_new.paste(img_twibbon, (0, 0), img_twibbon)

        
        
        img_twibbon.getdata()

        datas = []

        for item in datas:
         if item[0] >= 255 and item[1] >= 255 and item[2] >= 255 :
            datas.append((255, 255, 255, 0))
         else:
            datas.append(item)

        img_twibbon.putdata(datas)
        
        
        
        bytes = io.BytesIO()
        img_new.save(bytes, format='PNG')
        bytes.seek(0)
        img_new.save("./tes.png")
        return send_file(bytes, mimetype='image/png')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
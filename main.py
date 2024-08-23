from flask import Flask
from flask import *
from PIL import Image
import io
import base64

app = Flask(__name__)

#router awal
@app.route('/')
def render():
    return render_template('main.html')

#mengakses route get untuk mendapatkan file image 
@app.route("/get", methods= ["POST"])
def receive() :
    # jika method post maka akan mengeksekusi perintah
    if request.method == "POST" :
        #mengambil hasil inputan gambar user
        f = request.files['file']

        #membuka image ke pillow
        img_req = Image.open(f).copy().convert("RGBA")
        img_twibbon = Image.open("./static/ImagesTwibbon/twibbon1.png").copy().convert("RGBA")
        img_new = Image.new("RGBA", (img_twibbon.width, img_twibbon.height)).copy()

        #meresize image user sesuai dengan ukuran twibbon
        resize = img_req.resize((int(img_new.width), int(img_new.height)))

        #menampilkan gambar twibbon dan user
        img_new.paste(resize, (0, 0), resize)
        img_new.paste(img_twibbon, (0, 0), img_twibbon)
        
        #mengubah image menjadi base64 / binary
        bytes = io.BytesIO()
        img_new.save(bytes, format='PNG')
        bytes.seek(0)

        #mensave image ke local
        img_new.save("./here_the_image.png")

        #mereturn hasil gambar base64
        return send_file(bytes, mimetype='image/png', download_name='%s.png' % f.filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
from flask import Flask,render_template,request
import qrcode 
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

qr = qrcode.QRCode (
    version=1,
    box_size=10,
    border=5
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.form.get('link')
    # qr.make(fit=True)
    # img = qr.make_image(fill_color='white',back_color=(48, 48, 53))
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    
    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')  
    
    return render_template('index.html', data=base64_img)  

if __name__ == '__main__':
    app.run(debug=True)
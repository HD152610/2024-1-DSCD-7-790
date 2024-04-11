# 2024-1-DSCD-7-790

# 240411 플라스크- html로 넘기기까지만
# cmd -pip install flask 요

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('qr.html')

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/mypage.html')
def mypage():
    return render_template('mypage.html')

@app.route('/qr.html')
def qr():
    return render_template('qr.html')

if __name__ == '__main__':
    app.run(debug=True)

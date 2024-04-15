# 2024-1-DSCD-7-790

# 240415 최초 페이지 추가, 회원가입 정보 넘기는 거 구현 못함
# cmd -pip install flask,mysql 요

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

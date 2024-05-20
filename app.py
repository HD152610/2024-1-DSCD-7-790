from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hi.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/qr')
def qr():
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

if __name__ == '__main__':
    app.run(debug=True)


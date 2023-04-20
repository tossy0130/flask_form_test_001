from flask import Flask, render_template, request, url_for, redirect , session 
import os

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit_func', methods=['POST'])
def submit_func():
    # === フォームから値取得
    name = request.form['name']
    gender = request.form['gender']
    feedback = request.form['feedback']
    
    # === 値　保存
    ### === session の値をインクリメント
    session['count'] = session.get('count', 0) + 1
    
    return redirect(url_for('thanks'))

if __name__ == '__main__':
    app.run(debug=True)

    
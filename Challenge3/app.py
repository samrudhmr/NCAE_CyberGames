from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'super_secret_redundant_key'

@app.route('/', methods=['GET'])
def index():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password', '')
        if len(password) == 500:
            return render_template('error_trap.html')
        else:
            # Be passive-aggressive
            msg = f"Oh, that was only {len(password)} characters. We explicitly asked for 500. It's not that hard to follow instructions."
            flash(msg, 'error')
            return render_template('login.html')
            
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template

app = Flask(__name__)

# The secret flag for the CTF challenge
FLAG = "NCAE{client_side_security_is_no_security}"

@app.route('/')
def lobby():
    return render_template('index.html')

@app.route('/vip', methods=['GET', 'POST'])
def vip():
    # In a real app, we would check for a session/cookie/token here.
    # But this is "The VIP Velvet Rope", where security is nonexistent!
    return render_template('vip.html', flag=FLAG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

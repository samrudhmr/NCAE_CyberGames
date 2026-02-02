from flask import Flask, request, make_response, render_template

app = Flask(__name__)

# The secret flag for the CTF challenge
FLAG = "NCAE{this_is_the_flag}"

@app.route('/')
def index():
    # Get the role from cookie, default to None if not set
    role = request.cookies.get('role')
    
    # If no cookie exists, set it to 'guest'
    if role is None:
        response = make_response(render_template('index.html', role='guest', flag=None))
        response.set_cookie('role', 'guest')
        return response
    
    # Check if user is admin
    if role == 'admin':
        return render_template('index.html', role='admin', flag=FLAG)
    else:
        return render_template('index.html', role='guest', flag=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

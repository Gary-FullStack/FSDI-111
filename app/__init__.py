from flask import Flask

app = Flask(__name__)


@app.route('/aboutme', methods=['GET'])
def about_me():
    heres_me={'firstname': 'Gary', 'lastname': 'M.', 'hobbies': 'pc-gaming' }
    return (heres_me)

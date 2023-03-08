from flask import Flask

app = Flask(__name__)

@app.get("/")
def about_me():
    me = {

        "first_name": "Gary",
        "last_name" :  "M",
        "hobbies" :   "pc-gaming",
        "active":  True
    }

    return me 
from flask import Flask, render_template, request
from modelFunc import process
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_reponse():
    userText = request.args.get('msg')

    return str(process(userText))

if __name__ == "__main__":
    app.run(debug=True)
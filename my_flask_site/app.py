from flask import Flask

app = Flask(__name__)

#MySQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Godisalwaysgood20@localhost/bible_leaderboard'

@app.route("/")
def hello_world():
    return "<p>Connected to my SQL!</p>"

if __name__ == "__main__":
    app.run(debug = True)
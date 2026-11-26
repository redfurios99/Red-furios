from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Ciao, sono Red Furios</h1>
    <p>tu non sai quanto sei importante per me</p>
    <p>credo neanche io capirei</p>
    """

if __name__ == "__main__":
    app.run()

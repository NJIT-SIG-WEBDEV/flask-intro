from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def hello():
	return "Hello, world!"

if __name__ == "__main__":
	app.run(host="127.0.0.1")
